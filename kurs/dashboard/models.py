from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY = (
    ('Верхній одяг', 'Верхній одяг'),
    ('Взуття', 'Взуття'),
    ('Штани', 'Штани'),
    ('Категорія', 'Категорія'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, null=True, choices=CATEGORY)
    quanity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Товар'
     

    def __str__(self):
        return f'{self.category}  {self.name} Кількість: {self.quanity}'
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quanity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'{self.product} замовив(-ла) {self.staff.username}'