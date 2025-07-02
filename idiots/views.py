from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import IdiotsCreationForm


class RegisterView(CreateView):
    template_name = 'idiots/login.html'
    form_class = IdiotsCreationForm
    success_url = reverse_lazy('catalog/home.html')
