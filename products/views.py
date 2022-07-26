from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/productlist.html'
    context_object_name = 'products'


    def __str__(self):
        return self.title
