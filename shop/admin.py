from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from django import forms

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','category','description','price','image_show','image2']
    list_display_links = ['id','name','slug','category', 'description','price','image_show','image2']
    search_fields = ['name',]
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src = '{}' width = '200' height = '200' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"



@admin.register(Svyaz)
class SvyazAdmin(admin.ModelAdmin):
    list_display = ['id','message','number','email','datetime']
    list_display_links = ['id','message','number','email','datetime']
    search_fields = ['datetime',]

