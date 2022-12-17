from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','created','in_stock'] 
    list_filter = ['in_stock']  
    list_editable = ['price','in_stock']
    prepopulated_fields = {'slug': ('name',)}    
    
admin.site.register(OrderItem) 
admin.site.register(Order)
admin.site.register(ShippingAdress)    