from django.contrib import admin
from django.urls import path, include
from .views import imagem


#direciona todas urls de galeria sem precisar criar varios path nas urls.py da configuracao
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),    
    path('imagem/', imagem),
]