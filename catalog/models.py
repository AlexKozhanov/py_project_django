from django.db import models


class Category(models.Model):
    """Класс Категория"""
    # название, описание
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        # help_text='Введите название категории'
    )
    description = models.TextField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Описание')

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
        verbose_name='Название')
    description = models.TextField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Описание')
    png = models.ImageField(
        upload_to='products/photo',
        blank=True,
        null=True,
        verbose_name='Фото')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        default=None,
        verbose_name='Категория',
        null=True,
        blank=True,
        help_text='Выберите название Категории')
    price = models.FloatField(
        max_length=100,
        verbose_name='Цена')
    created_at = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата создания')
    updated_at = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата последнего изменения')
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        default=0)


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price', 'created_at', 'updated_at']
        #permissions = [('как будет сохранено'),('как будет выглядеть в панели администратора'),]
        #permissions = [('name_my_permission', 'Name my permission'),]

    #      ГРУППА - products moderator
    #     Кастомная роль - can_unpublish_product — может отменять публикацию продукта
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
        ]

    def __str__(self):
        return self.name
