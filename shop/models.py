from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Type(models.Model):
    type = models.CharField(default='no type', max_length=100)

    def __str__(self):
        return self.type

class Good(models.Model):
    title = models.CharField(default='clothing item', max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, blank=True,upload_to='post_pics')
    price = models.DecimalField(default=30.00, max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=1000)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
