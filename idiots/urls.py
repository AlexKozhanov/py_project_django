from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from idiots.apps import IdiotsConfig

from idiots.views import RegisterView

app_name = IdiotsConfig.name

urlpatterns = [
    path('register/',
         RegisterView.as_view(),
         name='register'),
    path('login/',
         LoginView.as_view(template_name='idiots/login.html'),
         name='login'),
    path('logout/',
         # LoginView.as_view(next_page='catalog/home.html'),
         LoginView.as_view(next_page='catalog/home.html'),
         name='logout'),

]