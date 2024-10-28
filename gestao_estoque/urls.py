from django.urls import path
from .views import (
    ProdutosListView,
    ProdutosCreateView,
    ProdutosRemoveView,
    ProdutosUpdateView
)

urlpatterns = [
    path('', ProdutosListView.as_view(), name='produtos'),
    path('create/', ProdutosCreateView.as_view(), name='produto-create'),
    path('update/<int:pk>/', ProdutosUpdateView.as_view(), name='produto-update'),
    path('remove/<int:pk>/', ProdutosRemoveView.as_view(), name='produto-remove'),
]
