from django.db import models


class Category(models.Model):
    """Класс Категория"""
    # название, описание
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Введите название категории')
    description = models.TextField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Описание',
        help_text='Введите описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', 'description']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Класс Продукты"""
    # наименование, описание, изображение, категория, цена за покупку, дата создания, дата последнего изменения
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        help_text='Введите название продукта')
    description = models.TextField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Описание',
        help_text='Введите описание продукта')
    png = models.ImageField(
        upload_to='products/photo',
        blank=True,
        null=True,
        verbose_name='Фото',
        help_text='Загрузите фото')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        default=None,
        verbose_name='Категория',
        help_text='Введите категорию продукта',
        null=True,
        blank=True)
    price = models.FloatField(
        max_length=100,
        verbose_name='Цена',
        help_text='Введите цену продукта')
    created_at = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата создания',
        help_text='Введите  продукта')
    updated_at = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата последнего изменения',
        help_text='Введите  продукта')
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'updated_at']

    def __str__(self):
        return self.name
