"""rataoweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from rataoapp.views import materiais, novo_material, home, editar_material, editar_local,novo_local,locais,nova_marca,marcas,editar_marca
from rataoapp.views import classes,nova_classe, editar_classe
from rataoweb import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materiais/', materiais, name='materiais'),
    path('novo_material/', novo_material, name='novo_material'),
    path('home/', home, name='home'),
    path('home/', home, name='home'),
    path('novo_local/', novo_local, name='novo_local'),
    path('nova_classe/', nova_classe, name='nova_classe'),
    path('locais/', locais, name='locais'),
    path('marcas/', marcas, name='marcas'),
    path('classes/', classes, name='classes'),
    path('nova_marca/', nova_marca, name='nova_marca'),
    path('editar_local/<int:codigo>', editar_local,name='editar_local'),
    path('editar_material/<int:item>', editar_material,name='editar_material'),
    path('editar_marca/<int:codigo>', editar_marca,name='editar_marca'),
    path('editar_classe/<int:codigo>', editar_classe,name='editar_classe'),

    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
