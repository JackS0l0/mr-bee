from django.shortcuts import render
from products.models import Products
def index(request):
    data={
        'title': 'Mr.Bre - home',
        'products':Products.objects.all().order_by('-date')[0:12],
    }
    return render(request,'index.html',data)