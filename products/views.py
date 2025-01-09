from django.shortcuts import render
from .models import Products
from django.views.generic import DetailView,ListView
class ProductDeatilView(DetailView):
    model = Products
    template_name = 'post.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        data=super(ProductDeatilView,self).get_context_data(**kwargs)
        data['title']=self.object.name
        return data