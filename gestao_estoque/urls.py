from django.urls import path
from .views import (
    HomeView,

    ProdutosListView,
    ProdutosCreateView,
    ProdutosRemoveView,
    ProdutosUpdateView,

    TiposListView,
    TiposCreateView,
    TiposUpdateView,
    TiposRemoveView,

    MarcasListView,
    MarcasCreateView,
    MarcasUpdateView,
    MarcasRemoveView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='estoque'),

    path('produtos/', ProdutosListView.as_view(), name='produtos'),
    path('produtos/create/', ProdutosCreateView.as_view(), name='produto-create'),
    path('produtos/update/<int:pk>/', ProdutosUpdateView.as_view(), name='produto-update'),
    path('produtos/remove/<int:pk>/', ProdutosRemoveView.as_view(), name='produto-remove'),

    path('tipos-produtos/', TiposListView.as_view(), name='tipos'),
    path('tipos-produtos/create/', TiposCreateView.as_view(), name='tipos-create'),
    path('tipos-produtos/update/<int:pk>/', TiposUpdateView.as_view(), name='tipos-update'),
    path('tipos-produtos/remove/<int:pk>/', TiposRemoveView.as_view(), name='tipos-remove'),

    path('marcas-produtos/', MarcasListView.as_view(), name='marcas'),
    path('marcas-produtos/create/', MarcasCreateView.as_view(), name='marcas-create'),
    path('marcas-produtos/update/<int:pk>/', MarcasUpdateView.as_view(), name='marcas-update'),
    path('marcas-produtos/remove/<int:pk>/', MarcasRemoveView.as_view(), name='marcas-remove'),
]