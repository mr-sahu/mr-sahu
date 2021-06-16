from django.contrib import admin
from .models import Product
from .models import Category
# Register your models here.
@admin.register(Product)
class Adminproduct(admin.ModelAdmin):
    list_display=['id','name','price','description','image','category']

@admin.register(Category)
class Admincategory(admin.ModelAdmin):
    list_display=['id','name']