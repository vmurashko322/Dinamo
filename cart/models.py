from django.db import models
from movies.models import Movie

class OrderDetail(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    email=models.EmailField()
    adress=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    pays=(
        ('0', 'выберите вариант оплаты'),
        ('1', 'наличными курьеру'),
        ('2','картой курьеру'),
        ('3','картой рассрочки')
    )
    pay_method=models.CharField(choices=pays, max_length=1)
    order_date=models.DateTimeField(auto_now_add=True)
    delivery_date=models.DateTimeField(auto_now=False)

    class Meta:
        ordering=('-order_date',)
        verbose_name='заказ'
        verbose_name_plural='заказы'

    def __str__(self):
        return '{}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order=models.ForeignKey(OrderDetail, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Movie, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price*self.quantity