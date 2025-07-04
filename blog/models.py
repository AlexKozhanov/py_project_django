from django.db import models


class Blog(models.Model):
    """Класс Блог"""
    # заголовок, содержимое, превью (изображение), дата создания, признак публикации (булевое поле), количество просмотров.
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
        help_text='Введите заголовок Блога')
    content = models.TextField(
        blank=True,
        null=True,
        max_length=100,
        verbose_name='Содержимое',
        help_text='Введите содержимое Блога')
    png = models.ImageField(
        upload_to='products/photo',
        blank=True,
        null=True,
        verbose_name='Превью (изображение),',
        help_text='Загрузите фото')
    creation_date = models.DateField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата создания',
        help_text='Дата создания')
    publication = models.BooleanField( # bool
        verbose_name='Признак публикации',
        help_text='Да/Нет')
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров",
        help_text="Укажите количество просмотров",
        default=0)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги-Андердоги'
        ordering = ['title', 'content', 'png', 'creation_date', 'publication']

    def __str__(self):
        return self.title
