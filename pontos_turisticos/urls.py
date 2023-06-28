# Configurações da url do Projeto (setup)
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
#pegar na documentação
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from enderecos.api.viewsets import EnderecoViewSet


#Configurando as rotas de acesso aos endpoints
router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracoesViewSet)
router.register(r'enderecos', EnderecoViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
