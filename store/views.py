from django.shortcuts import render
from .models import Product
from .models import Category
 
#from .models import Category
# Create your views here.
def home(request):
    products=None
    categories=Category.get_all_categories()
    categoryID=request.GET.get('categories')
    print(categoryID)
    if categoryID:
        products=Product.get_all_products_by_categoryid(categoryID)
    else:
        products=Product.get_all_products()
    print(categoryID)

    
    data={}
    data['products']=products
    data['categories']=categories
    return render(request,'store/home.html',data)