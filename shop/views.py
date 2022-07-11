from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *

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

class ItemDetailView(DetailView):
    template_name = 'shop/item_detail.html'
    model = Good

class CartListView(ListView):
    model = Good
    template_name = 'shop/cart.html'
    context_object_name = 'goods'
    ordering = ['-date_added']

def product(request, pk):
    product = Good.objects.get(id=pk)

    if request.method == 'POST':
        product = Good.objects.get(id=pk)
        #Get user account information
        try:
        	customer = request.user.customer
        except:
        	device = request.COOKIES['device']
        	customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity = int(orderItem.quantity) + int(request.POST['quantity'])
        orderItem.save()

        return redirect('cart')

    context = {'product':product}
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
