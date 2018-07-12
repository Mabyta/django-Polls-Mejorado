from django.contrib import admin
from django.urls import path, include   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('super_polls.urls')),
    path('user/', include('accounts.urls')),
]
