from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from idiots.models import Idiots

class IdiotsRegisterForm(UserCreationForm):
    class Meta:
        model = Idiots
        # exclude = ("views_counter",)
        fields = ('email', 'password1', 'password1')

    # def __init__(self, *args, **kwargs):
    #     super(ProductForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Введите название продуктааа'
    #     })
    #     self.fields['description'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Введите описание продуктааа'
    #     })
    #     self.fields['png'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Приложите картинку продуктааа'
    #     })
    #     self.fields['category'].widget.attrs.update({
    #         'class': 'form-control',
    #         # 'placeholder': 'Выберите название Категории'
    #     })
    #     self.fields['price'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Введите цену продуктааа'
    #     })
    #     self.fields['created_at'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Введите дату создания продуктааа'
    #     })
    #     self.fields['updated_at'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Введите дату редактирования продуктааа'
    #     })

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     lowered = name.lower()
    #     for word in cuss:
    #         if word in lowered:
    #             raise ValidationError('Имя Продукта запрещено')
    #     return name

