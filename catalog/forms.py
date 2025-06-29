from django.forms import ModelForm, \
                         BooleanField
from django.core.exceptions import ValidationError

from catalog.models import Product, Category


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("views_counter",)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название продуктааа'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')

        # if Product.objects.filter(name=name, category=category).exist():
        if Product.objects.get(name=name, category=category):
            raise ValidationError('Продукт с таким Именем и Категорией уже существует')
        return cleaned_data


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название категорииии'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание категорииии'
        })

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name and description and name == description:
            self.add_error(field='name', error='Имя и описание не могут иметь одинаковое значение')

    # def clean_"имя_атрибута_класса"(self):
    # Дочтать поле значения
    # Проверить его