from django.contrib import admin
from django.urls import path
from super_polls.views import encuestas_view,resultados_view,inicio_view

urlpatterns = [
    path('inicio/', inicio_view, name='inicio'),
    path('encuestas/', encuestas_view),
    path('resultados/', resultados_view),
]
