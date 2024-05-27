from django.db import models


# from django.conf import settings
# from django.contrib.auth.models import User




class Category(models.Model):
    name = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(blank=True, null=True, verbose_name='Картинка')
    image2 = models.ImageField(blank=True, null=True, verbose_name='Картинка2')

    class Meta():
        verbose_name_plural = "2. Категории"
        verbose_name = "Категорию"

    def __str__(self):
        return f"{self.id}, {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя товара')
    slug = models.SlugField(null=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория товара')
    description = models.TextField(null=True, blank='None', verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(blank=True, null=True, verbose_name='Картинка')
    image2 = models.ImageField(blank=True, null=True, verbose_name='Картинка2')

    class Meta():
        verbose_name_plural = "1. Товары"
        verbose_name = "Товар"

    # def __str__(self):
    #     return f"{self.id}, {self.name}, Категория продукта - {self.category_id}"

    def __str__(self):
        return 'Obj: {}'.format(self.id)


class Svyaz(models.Model):
    message = models.TextField(verbose_name='Сообщение')
    number = models.TextField()
    email = models.TextField()
    datetime = models.TextField()

    class Meta():
        verbose_name_plural = "3. Сообщения от пользователей"
        verbose_name = "Запись"