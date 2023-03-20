from django.urls import path
from . import views


urlpatterns = [
    path('', views.about, name='home'),
    path('recommendations', views.recommendations, name='recommendations'),
    path('friends', views.friends, name='friends'),
    path('registration', views.registration, name='registration'),
    path('account', views.account, name='account'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
]