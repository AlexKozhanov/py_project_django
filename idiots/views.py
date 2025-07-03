from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import IdiotsCreationForm


class RegisterView(CreateView):
    template_name = 'idiots/register.html'
    form_class = IdiotsCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        idiot = form.save()
        self.send_welcome_email(idiot.email)
        return super().form_valid(form)

    def send_welcome_email(self, idiot_email):
        subject = 'Добро пожаловать в наш сервис!'
        message = 'Спасибо т**е, что зарегистрировался в нашем сервисе!'
        from_email = 'iVasya2033@yandex.ru'
        recipient_list = [idiot_email, ]
        send_mail(subject, message, from_email, recipient_list)