from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import    ListView,\
                                    DetailView,\
                                    CreateView,\
                                    UpdateView,\
                                    DeleteView
from django.urls import reverse_lazy, reverse

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        name = request.POST.get("name")
        text = request.POST.get("text")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено с текстом '{text}'. Мы свяжемся с вами по почте {mail}")
    return render(request, 'catalog/contacts.html')

class CatalogListView(ListView):
    model = Product
    # app_name/<modul_name>_<action>
    # catalog/product_detail.html

class CataDetailListView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class ProductCreateView(CreateView):
    model = Product
    fields = ("name", "description", "png", "category", "price", "created_at", "updated_at")
    success_url = reverse_lazy('catalog:product_list')
    # success_url = reverse_lazy('<Название приложения>:<Название url>')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("name", "description", "png", "category", "price", "created_at", "updated_at")
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')