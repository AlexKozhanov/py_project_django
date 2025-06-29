from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import   home, \
                            contacts,\
                            CatalogListView,\
                            CataDetailListView,\
                            ProductCreateView,\
                            ProductUpdateView, \
                            ProductDeleteView, \
                            CategoryListView, \
                            CategoryCreateView, \
                            CategoryUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/', CatalogListView.as_view(), name='product_list'),
    path('catalog/<int:pk>/', CataDetailListView.as_view(), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),

    path('catalog/category/', CategoryListView.as_view(), name='category_list'),
    path('catalog/category/new', CategoryCreateView.as_view(), name='category_create'),
    path('catalog/category/<int:pk>/update', CategoryUpdateView.as_view(), name='category_update'),
]
