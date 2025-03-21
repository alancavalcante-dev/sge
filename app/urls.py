from django.contrib import admin
from django.urls import path, include
from recibo import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recibo/', views.Recibo.as_view(), name='recibo'),
    
    path('estoque/', include('gestao_estoque.urls')),
    path('caixa/', include('caixa.urls')),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
