from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View, TemplateView
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .forms import CheckoutForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class DeleteOrderItemAPI(APIView):
    def get(self, request, pk, format=None):
        order_item = get_object_or_404(OrderItem, id=pk)
        deleted = False
        if order_item:
            order_item.delete()
            deleted = True
        data = {
            'deleted': deleted,
        }
        return Response(data)

class IncreaseOrderItemAPI(APIView):
    def get(self, request, pk, format=None):
        order_item = get_object_or_404(OrderItem, id=pk)
        updated = False
        if order_item:
            print(order_item.quantity)
            order_item.quantity += 1
            order_item.save()
            updated = True
        data = {
            'updated': updated,
        }
        return Response(data)

class DecreaseOrderItemAPI(APIView):
    def get(self, request, pk, format=None):
        order_item = get_object_or_404(OrderItem, id=pk)
        updated = False
        if order_item:
            order_item.quantity -= 1
            order_item.save()
            if order_item.quantity < 1:
                order_item.delete()
            updated = True
        data = {
            'updated': updated,
        }
        return Response(data)

class SaveDeliveryInfoAPI(APIView):
    def get(self, request, *args, **kwargs):
        full_name = self.request.GET.get('full_name')
        phone = self.request.GET.get('phone')
        email = self.request.GET.get('email')
        country = self.request.GET.get('country')
        city = self.request.GET.get('city')
        address = self.request.GET.get('address')
        zip = self.request.GET.get('zip')
        delivery_info = DeliveryInfo(
            full_name = full_name,
            phone = phone,
            email = email,
            country = country,
            city = city,
            address = address,
            zip = zip,
        )
        delivery_info.save()
        order_id = request.COOKIES['order_id']
        order = Order.objects.get(order_id=order_id)
        try:
            DeliveryInfo.objects.get(order=order).delete()
        except:
            pass
        order.delivery_info = delivery_info
        order.save()

        return Response(self.request.GET)

def home(request):
    context = {}
    goods = Good.objects.all().order_by('-id')
    context['goods'] = goods
    try:
        order_id = request.COOKIES['order_id']
        order, created = Order.objects.get_or_create(order_id=order_id, complete=False)

        context['order'] = order
    except:
        pass
    print(goods)
    return render(request, 'shop/home.html', context)

def product(request, pk):
    product = Good.objects.get(id=pk)
    context = {}
    if request.method == 'POST':
        product = Good.objects.get(id=pk)
        order_id = request.COOKIES['order_id']
        order, created = Order.objects.get_or_create(order_id=order_id, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, size=request.POST['size'])
        orderItem.quantity = int(orderItem.quantity) + int(request.POST['quantity'])
        orderItem.save()

        return redirect('cart')

    context = {'product':product}
    try:
        order_id = request.COOKIES['order_id']
        order = Order.objects.get(order_id=order_id)
        context['order'] = order
    except:
        pass
    return render(request, 'shop/product.html', context)

def cart(request):
    try:
        order_id = request.COOKIES['order_id']
        order, created = Order.objects.get_or_create(order_id=order_id, complete=False)
    except:
        return redirect('shop-home')

    context = {'order':order}
    return render(request, 'shop/cart.html', context)

class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order_id = self.request.COOKIES['order_id']
        except:
            return redirect('shop-home')
        order = Order.objects.get(order_id=order_id)
        form = CheckoutForm()
        context = {
            'form': form,
            'order': order,
            "STRIPE_PUBLIC_KEY": 'pk_test_51LLrLoCihPRd6C0fNQKhJ73pM1QvCVEd6Qn40jWbJjFFFz49F6IzK5j2cp6R9wOo1UG0JExS5xmufj9YC8seUjKO00lu1e17uF',
        }
        return render(self.request, 'shop/checkout.html', context)
        if form.is_valid():
            return redirect('checkout')

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        order_id = request.COOKIES['order_id']
        order = Order.objects.get(order_id=order_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        line_items = []
        order_items = OrderItem.objects.all().filter(order=order)
        stock_changes = ""
        for order_item in order_items:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(order_item.product.price*100),
                    'product_data': {
                        'name': order_item.product.title,
                        "description": f'Type: {order_item.product.type}; Size: {order_item.size}',
                    },
                },
                'quantity': order_item.quantity,
            })
            stock_changes += f'{order_item.product.id}_{order_item.size}_ {order_item.quantity}/'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            metadata={
                "product_id": str([order_item.product.id for order_item in order_items]),
                "order_id": order_id,
                "stock_changes": str(stock_changes)
            },
            mode='payment',
            success_url=f'{YOUR_DOMAIN}/deletecookies/{order_id}',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


def order(request, pk):
    order = Order.objects.get(order_id=pk)
    context = {
        'order': order,
    }

    return render(request, 'shop/order.html', context)

def cancel(request):
    return render(request, 'shop/cancel.html')


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        session = event['data']['object']
        print(session)
        custromer_email = session["customer_details"]["email"]
        transaction_id = session["payment_intent"]
        order_id = session["metadata"]["order_id"]
        stock_changes = session["metadata"]["stock_changes"]
        stock_changes_split = [stock_change.split("_") for stock_change in stock_changes.split("/")]
        stock_changes_split.pop(-1)
        for stock_change in stock_changes_split:
            product = Good.objects.get(id=stock_change[0])
            stock = product.stock.split(";")
            new_stock = ''
            for stock_i in stock:
                if stock_i.split("_")[0] == stock_change[1]:
                    stock_i_new = f'{stock_i.split("_")[0]}_{int(stock_i.split("_")[1])-int(stock_change[2])};'
                    new_stock += stock_i_new
                else:
                    new_stock += stock_i + ';'
            product.stock = new_stock[:-1:]
            product.save()

        order = Order.objects.get(order_id=order_id)
        order.transaction_id = transaction_id
        order.save()
        send_mail(
            subject="here's your product",
            message="thanks for the puschase",
            recipient_list=[custromer_email],
            from_email='test1486745321@gmail.com'
        )

    response = HttpResponse(status=200)
    return response

def delete_user_cookies(request, order_id):
    response = HttpResponseRedirect(reverse('order', args=(order_id,)))
    response.delete_cookie('order_id')
    return response
