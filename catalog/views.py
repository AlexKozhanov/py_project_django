from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

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

def catalog(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/catalog.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'catalog/product_detail.html', context)