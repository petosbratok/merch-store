from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View, TemplateView
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .forms import CheckoutForm
import stripe
from django.conf import settings

stripe.api_key = 'sk_test_51LLrLoCihPRd6C0f9H2L00Nq6AAjvSwLkDykjVGJ0LdLs03mldDvTsiZLhS8ASax9HHl7wTiDoffSyIQMQMk1ZJw00rp5AoRxI'


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

def home(request):
    context = {}
    goods = Good.objects.all().order_by('-id')
    context['goods'] = goods

    try:
        customer = request.user.customer
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        context['order'] = order
    print(goods)
    return render(request, 'shop/home.html', context)

def product(request, pk):
    product = Good.objects.get(id=pk)

    if request.method == 'POST':
        product = Good.objects.get(id=pk)
        #Get user account information
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity = int(orderItem.quantity) + int(request.POST['quantity'])
        orderItem.save()

        return redirect('cart')

    context = {'product':product}
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    context['order'] = order
    return render(request, 'shop/product.html', context)

def cart(request):
	try:
		customer = request.user.customer
	except:
		device = request.COOKIES['device']
		customer, created = Customer.objects.get_or_create(device=device)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)


	context = {'order':order}
	return render(request, 'shop/cart.html', context)

class CheckoutView(View):
    def get(self, *args, **kwargs):
        device = self.request.COOKIES['device']
        order = Order.objects.get(customer=Customer.objects.get(device=device))
        form = CheckoutForm()
        context = {
            'form': form,
            'order': order,
        }
        return render(self.request, 'shop/checkout.html', context)
        if form.is_valid():
            return redirect('checkout')

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            country = form.cleaned_data.get('country')
            city = form.cleaned_data.get('city')
            address = form.cleaned_data.get('address')
            zip = form.cleaned_data.get('zip')

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
            device = self.request.COOKIES['device']
            order = Order.objects.get(customer=Customer.objects.get(device=device))
            try:
                DeliveryInfo.objects.get(order=order).delete()
            except:
                pass
            order.delivery_info = delivery_info
            order.save()
            return redirect('checkout')
        return redirect('checkout')

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        device = self.request.COOKIES['device']
        order = Order.objects.get(customer=Customer.objects.get(device=device))
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        line_items = []
        for order_item in OrderItem.objects.all().filter(order=order):
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(order_item.product.price*100),
                    'product_data': {
                        'name': order_item.product.title,
                        # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                    },
                },
                'quantity': order_item.quantity,
            })
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            metadata={
                "product_id": 'no data'
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

class ProductLandingPageView(TemplateView):
    template_name = "shop/landing.html"

    def get_context_data(self, **kwargs):
        product = Good.objects.get(id=1)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": 'pk_test_51LLrLoCihPRd6C0fNQKhJ73pM1QvCVEd6Qn40jWbJjFFFz49F6IzK5j2cp6R9wOo1UG0JExS5xmufj9YC8seUjKO00lu1e17uF'
        })
        return context

def success(request):
    return render(request, 'shop/success.html')

def cancel(request):
    return render(request, 'shop/cancel.html')
