from django.contrib import admin
from django.urls import path
from super_polls.views import encuestas_view,resultados_view,inicio_view

urlpatterns = [
    path('', inicio_view, name='inicio'),
    path('Home/', inicio_view, name='home'),# Se llama = {% url 'home' %} y me lo pide obligatoriamente accounts >:(
    path('inicio/', inicio_view, name='inicio'),# Se llama = {% url 'inicio' %}
    path('encuestas/', encuestas_view, name='encuestas'),# Se llama = {% url 'encuestas' %}
    path('resultados/', resultados_view, name='resultados'),# Se llama = {% url 'resultados' %}   :)  >u<   UNA VEZ MAS... Tramposa!! Buajajaja
]
