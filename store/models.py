from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.name + ' ' + self.email
        

class Category(models.Model):
    title = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    
    #def get_absolute_url(self):
    #    return reverse("store:category_list", args=[ self.slug])
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title())
        return super().save(*args,**kwargs)    
        
        
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=4,decimal_places=2)  
    slug = models.SlugField(max_length=255,unique=True)
    img = models.ImageField(upload_to='images/')
    describtions = models.TextField(blank=True)
    in_stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.name
    
    #def get_absolute_url(self):
    #    return reverse('store:product_detail',args=[ self.slug])  
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)    
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=25)
    
    def __str__(self):
        return self.transaction_id
    
    
class OrderItem(models.Model):
    product =models.ForeignKey(Product, on_delete=models.CASCADE)  
    order = models.ManyToManyField(Order)
    order_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.product.name + " " + self.quantity
    
    
class ShippingAdress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zib_code = models.CharField(max_length=255)  
    
      