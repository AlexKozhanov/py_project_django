from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, \
                                 DetailView, \
                                 CreateView, \
                                 UpdateView, \
                                 DeleteView
from django.urls import reverse_lazy, reverse

from blog.models import Blog


class BlogListView(ListView):  # Основной экран
    model = Blog
    template_name = 'blog_list.html'
    # app_name/<modul_name>_<action>
    # catalog/product_detail.html
    def get_queryset(self):
        # фильтрация только опубликованных статей
        return super().get_queryset().filter(publication=True)


class BlogDetailListView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'png', 'creation_date', 'publication')
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')
    # success_url = reverse_lazy('<Название приложения>:<Название url>')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'png', 'creation_date', 'publication')
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_list')
