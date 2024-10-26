from django.contrib import admin
from django.urls import path
from recibo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recibo/', views.Recibo.as_view(), name='recibo'),

]
