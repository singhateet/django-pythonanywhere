from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True) #slug field because all our cateogries are going to be unique

    class Meta:
        verbose_name_plural = 'categories' #because in admin the Default is Categorys

     #because in admin the Default is category(1), category(2)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('list-category', args=[self.slug])
    
class Product(models.Model):

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)    
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-branded')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255) #slug field because all our products are goint to be unique
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='images/', default='no image')

    class Meta:
        verbose_name_plural = 'products' #because in admin the Default is Categorys

     #because in admin the Default is product(1), product(2)
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('product-info', args=[self.slug])








