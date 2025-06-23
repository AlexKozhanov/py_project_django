from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

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

class CataDetailListView(DetailView):
    model = Product

    # app_name/<modul_name>_<action>
    #catalog/product_detail.html
