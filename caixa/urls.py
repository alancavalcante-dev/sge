from django.urls import path
from .views import CaixaView



urlpatterns = [
    path('', CaixaView.as_view(), name='home')
]
