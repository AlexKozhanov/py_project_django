from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        name = request.POST.get("name")
        text = request.POST.get("text")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено с текстом '{text}'. Мы свяжемся с вами по почте {mail}")
    return render(request, 'catalog/contacts.html')
