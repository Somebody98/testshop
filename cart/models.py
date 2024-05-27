from django.db import models

class Order(models.Model):

    STATUSORDER_CHOICES = [
        ('N', 'В ожидании'),
        ('W', 'Принят'),
        ('C', 'Завершен'),
    ]

    number = models.CharField(max_length=500, verbose_name='Номер заказчика')
    address = models.CharField(max_length=500, verbose_name='Адрес')
    message = models.CharField(max_length=500, verbose_name='Сообщение', blank=True, null=True)
    price = models.CharField(max_length=100, verbose_name='Стоимость заказа')
    unicnum = models.CharField(max_length=100, verbose_name='Номер заказа')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    status = models.CharField(max_length=1, choices=STATUSORDER_CHOICES, verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = '1. Клиенты'

    def __str__(self):
        return '{}'.format(self.id)


class OrderItem(models.Model):
    product = models.CharField(max_length=150, verbose_name='Имя товара')
    price_1_product = models.CharField(max_length=100, verbose_name='Цена за 1 товар')
    quantity = models.IntegerField(verbose_name='Количество')
    price_all = models.CharField(max_length=100, verbose_name='Общая цена')
    id_order = models.CharField(max_length=100, verbose_name='Номер заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = '2. Заказы'

    def __str__(self):
        return '{}'.format(self.id)

