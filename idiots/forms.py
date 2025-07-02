from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from idiots.models import Idiots


class IdiotsCreationForm(UserCreationForm):
    phone_number = forms.CharField(
        max_length=35,
        # verbose_name='Телефон',
        required=False,
        help_text='Номер Телефона')
    username = forms.CharField(
        max_length=50,
        # verbose_name='Имя',
        required=True)
    usable_password = None


    class Meta:
        model = Idiots
        # exclude = ("views_counter",)
        fields = ('email',
                  'username',
                  'first_name',
                  'last_name',
                  'phone_number',
                  'password1',
                  'password2')

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

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер должен состоять только из цифр')
        return phone_number
