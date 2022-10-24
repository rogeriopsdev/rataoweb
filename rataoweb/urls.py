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
from django.urls import path
from django.views.static import serve

from rataoapp.views import mostrar_materiais, novo_material
from rataoweb import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mostrar_materiais/',mostrar_materiais, name='mostrar_materiais'),
    path('novo_material/',novo_material, name='novo_material'),
    path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
   ]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)