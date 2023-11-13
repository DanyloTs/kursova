from django.db import models

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


    def __str__(self):
        return f'{self.category}  {self.name} Кількість: {self.quanity}'