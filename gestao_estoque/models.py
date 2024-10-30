from django.db import models


class TipoProduto(models.Model):
    type = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='tipos/', null=True, blank=True)

    def __str__(self):
        return self.type


class MarcaProduto(models.Model):
    brand = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.brand


class Produto(models.Model):
    type = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    brand = models.ForeignKey(MarcaProduto, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=8 ,decimal_places=2)
    image = models.ImageField(upload_to='produtos/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
