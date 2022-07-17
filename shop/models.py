from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Type(models.Model):
    type = models.CharField(default='no type', max_length=100)
    generalType = models.CharField(default='shirt', max_length=100)
    def __str__(self):
        return self.type

class Good(models.Model):
    title = models.CharField(default='clothing item', max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    photo = models.ImageField(default='изображение_2022-07-10_235015707',upload_to='merch_pics')
    price = models.DecimalField(default=30.00, max_digits=10, decimal_places=2)
    stock = models.CharField(default='xs_100 s_100 m_100 l_100 xl_100', max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})


class DeliveryInfo(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
    	return str(self.id)

class Order(models.Model):
    delivery_info = models.ForeignKey(DeliveryInfo, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, default=9999999999999999)
    order_id = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
    	return str(self.id)

    @property
    def get_cart_total(self):
    	orderitems = self.orderitem_set.all()
    	total = sum([item.get_total for item in orderitems])
    	return total

    @property
    def get_cart_items(self):
    	orderitems = self.orderitem_set.all().order_by('id')
    	return orderitems

    @property
    def get_cart_length(self):
    	length = sum([item.quantity for item in self.orderitem_set.all()])
    	return length

class OrderItem(models.Model):
    product = models.ForeignKey(Good, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=2, blank=True, null=True)
    @property
    def get_total(self):
    	total = self.product.price * self.quantity
    	return total
