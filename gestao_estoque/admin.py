from django.contrib import admin
from .models import (
    TipoProduto,
    MarcaProduto,
    Produto
)


@admin.register(TipoProduto)
class TipoProdutoModelAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(MarcaProduto)
class MarcaProdutoModelAdmin(admin.ModelAdmin):
    list_display = ['brand']


@admin.register(Produto)
class ProdutoModelAdmin(admin.ModelAdmin):
    list_display = ['type__type', 'brand__brand', 'name', 'quantity', 'price']
