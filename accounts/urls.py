from django.urls import include, path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views


urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]