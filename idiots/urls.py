from django.urls import path
from django.contrib.auth.views import LoginView
from idiots.apps import IdiotsConfig

# from catalog.views import   home, \
#                             contacts,\
#                             ProductListView,\
#                             ProductDetailListView,\
#                             ProductCreateView,\
#                             ProductUpdateView, \
#                             ProductDeleteView, \
#                             CategoryListView, \
#                             CategoryDetailListView, \
#                             CategoryCreateView, \
#                             CategoryUpdateView

app_name = IdiotsConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html')),
    # path('contacts/', contacts, name='contacts'),
    # path('catalog/', ProductListView.as_view(), name='product_list'),

]