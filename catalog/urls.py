from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import   Home, \
                            Contacts,\
                            CatalogListView,\
                            CataDetailListView,\
                            ProductCreateView,\
                            ProductUpdateView, \
                            ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('catalog/', CatalogListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', CataDetailListView.as_view(), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
