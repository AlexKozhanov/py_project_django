from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from idiots.models import Idiots
# avatar, country, date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, password, phone_number, tg_name, user_permissions

class IdiotsCreationForm(UserCreationForm):
    # username = forms.CharField(
    #     max_length=50,
    #     # verbose_name='Имя',
    #     required=True)
    email = forms.EmailField(
        # unique=True,
        required=False,
        help_text='Mail')
    phone_number = forms.CharField(
        max_length=35,
        # verbose_name='Телефон',
        required=False,
        help_text='Номер Телефона')
    tg_name = forms.CharField(
        max_length=35,
        # verbose_name='Ник ТГ',
        required=False,
        help_text='Ник ТГ')
    avatar = forms.ImageField(
        # upload_to='idiots/avatars/',
        # verbose_name='Аватар',
        required=False,
        help_text='Аватар')
    country = forms.CharField(
        max_length=50,
        # verbose_name='Страна',
        required=False,
        help_text='Страна')
    #
    # usable_password = None


    class Meta:
        model = Idiots
        # exclude = ("views_counter",)
        # fields = ('username',
        #           'email',
        #           'first_name',
        #           'last_name',
        #           'phone_number',
        #           'password1',
        #           'password2')
        fields = (
            # 'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'tg_name',
            'avatar',
            'country',
            'password1',
            'password2',
                  )

    def __init__(self, *args, **kwargs):
        super(IdiotsCreationForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({
        #     'class': 'form-control',
        #     'placeholder': 'Введите логииин'
        # })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Приложите emaiiil'
        })
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Приложите first_name'
        })
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Приложите last_name'
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите телефоооон!'
        })
        self.fields['tg_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберите tg_name'
        })
        self.fields['avatar'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите avatar'
        })
        self.fields['country'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите country'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите password1'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите password2'
        })

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер должен состоять только из цифр')
        return phone_number
