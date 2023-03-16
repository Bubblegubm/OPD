from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('recommendations', views.recommendations),
    path('friends', views.friends),
    path('registration', views.registration),
    path('account', views.account),
]