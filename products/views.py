from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/productlist.html'
    context_object_name = 'products'
