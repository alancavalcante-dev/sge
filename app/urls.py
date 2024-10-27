from django.contrib import admin
from django.urls import path, include
from recibo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recibo/', views.Recibo.as_view(), name='recibo'),
    path('', include('caixa.urls')),

]
