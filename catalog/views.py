from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import \
    LoginRequiredMixin, \
    PermissionRequiredMixin
from django.views.generic import \
    ListView, \
    DetailView, \
    CreateView, \
    UpdateView, \
    DeleteView, \
    View

#CACHE
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache

from catalog.forms import ProductForm, ProductModeratorForm, CategoryForm
from catalog.models import Product, Category
from catalog.services import get_products_in_category


# class PublicationStatusProductView(LoginRequiredMixin, View):
#     def post(self, request, product_id):
#         product = get_object_or_404(Product, id=product_id)
#
#         if not request.user.has_perm('catalog.can_unpublish_product'):
#             return HttpResponseForbidden(
#                 'У вас нет права для - отмены статуса публикации продукта'
#             )
#
#         product.publication_status = request.POST.get('publication_status')
#         product.save()
#
#         return redirect('catalog:product_detail', product_id=product_id)


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        name = request.POST.get("name")
        text = request.POST.get("text")

        return HttpResponse(
            f"Спасибо, {name}! Сообщение получено с текстом '{text}'. Мы свяжемся с вами по почте {mail}")
    return render(request, 'catalog/contacts.html')

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    # app_name/<modul_name>_<action>
    # catalog/product_detail.html
    permission_required = 'catalog.view_product'

@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailListView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    # success_url = reverse_lazy('<Название приложения>:<Название url>')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def get_form_class(self):
        user = self.request.user
        if not user.has_perm('catalog.delete_product') or not user == self.object.owner:
            raise PermissionDenied


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'
    permission_required = 'catalog.view_category'

    def get_queryset(self):
        queryset = cache.get('category_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('category_queryset', queryset, 60 * 15)
        return queryset


class CategoryDetailListView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/category_detail.html'
    success_url = reverse_lazy('catalog:category_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        return self.object


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:category_list')
    permission_required = 'catalog.create_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_form.html'
    success_url = reverse_lazy('catalog:category_list')
    permission_required = 'catalog.change_category'

    # def get_success_url(self):
    #     return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])


class ProductByCategoryListView(ListView):
    template_name = 'catalog/category_products.html'
    context_object_name = 'productsbycategory'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_products_in_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        context['category'] = Category.objects.get(pk=category_id)
        return context
