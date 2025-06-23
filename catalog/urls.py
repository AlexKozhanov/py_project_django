from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import home, contacts, CatalogListView, CataDetailListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', CatalogListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', CataDetailListView.as_view(), name='product_detail')
]
