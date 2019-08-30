from django.views.generic.list import ListView
from .models import Product


class ProductListView(ListView):
   model = Product
   context_object_name = 'products'

   def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     context['products'] = Product.objects.filter(store__site=self.request.site)
     return context