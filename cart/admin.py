from django.contrib import admin
from .models import *

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['id','number','address','message','price','unicnum','created','status']
    list_display_links = ['id','number','address','message']
    list_editable = ['status']
    search_fields = ['created','id']

@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ['id','product','price_1_product','quantity','price_all','id_order']
    list_display_links = ['id','product']
    search_fields = ['id_order']