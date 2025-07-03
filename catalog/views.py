from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, \
                                 DetailView, \
                                 CreateView, \
                                 UpdateView, \
                                 DeleteView
from django.urls import reverse_lazy, reverse
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.forms import ProductForm, CategoryForm
from catalog.models import Product, Category


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


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    # app_name/<modul_name>_<action>
    # catalog/product_detail.html
    permission_required = 'catalog.view_product'


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
    permission_required = 'catalog.create_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     ProductFormet = inlineformset_factory(
    #         parent_model=Category,
    #         model=Product,
    #         form=CategoryForm,
    #         extra=1)
    #     if self.request.method == 'POST':
    #         context_data["formset"] = ProductFormet(self.request.POST, instance=self.object)
    #     else:
    #         context_data["formset"] = ProductFormet(instance=self.object)
    #     return context_data
    #
    # def form_valid(self, form):
    #     context_data = self.get_context_data()
    #     formset = context_data["formset"]
    #     if form.is_valid() and formset.is_valid():
    #         self.object = form.save()
    #         formset.instance = self.object
    #         formset.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'
    permission_required = 'catalog.view_category'


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
