from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .forms import CheckoutForm

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
        form = CheckoutForm()
        context = {
            'form': form,
        }
        return render(self.request, 'shop/checkout.html', context)
        if form.is_valid():
            print('form is valid')
            return redirect('checkout')

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('checkout')
        return redirect('checkout')
