from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views


urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),# Se llama = {% url 'signup' %}
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),# Se llama = {% url 'login' %}
    path('question/', accounts_views.question, name='question'),# Se llama = {% url 'question' %}
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),# Se llama = {% url 'loguot' %}
]
#creo que login deberia de ser la pagina que abra cuando corres polls , que opinas?
#creo que el usuario no registrado deberia poder ver pero solo poder ver y convencerse de registrarse