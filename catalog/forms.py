from django.forms import ModelForm, \
    BooleanField
from django.core.exceptions import ValidationError

from catalog.models import Product, Category

cuss = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


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
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание продуктааа'
        })
        self.fields['png'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Приложите картинку продуктааа'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': 'Выберите название Категории'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену продуктааа'
        })
        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату создания продуктааа'
        })
        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату редактирования продуктааа'
        })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        lowered = name.lower()
        for word in cuss:
            if word in lowered:
                raise ValidationError('Имя Продукта запрещено')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        lowered = description.lower()
        for word in cuss:
            if word in lowered:
                raise ValidationError('Описание Продукта запрещено')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price


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

    def clean_name(self):
        name = self.cleaned_data.get('name')
        lowered = name.lower()
        for word in cuss:
            if word in lowered:
                raise ValidationError('Имя Категории запрещено')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        lowered = description.lower()
        # if Product.objects.filter(name=name, category=category).exist():
        for word in cuss:
            if word in lowered:
                raise ValidationError('Описание Категории запрещено')
        return description

    # def clean_"имя_атрибута_класса"(self):
    # Достать поле значения
    # Проверить его


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        # exclude = ("views_counter",) # всё кроме
        fields = ("publication_status",) # перечисленные поля
