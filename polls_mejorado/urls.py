from django.contrib import admin
from django.urls import path, include   
from super_polls.views import encuestas_view,resultados_view,inicio_view

urlpatterns = [
    path('polls/', include('super_polls.urls')),
    path('admin/', admin.site.urls),
  
    
    #No se toca
    #matare al que lo toque
    #Al que lo toque se le aparece el diablo
    path('user/', include('accounts.urls')),
]
