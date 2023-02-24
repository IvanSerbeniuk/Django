from django.urls import path

from . import views

#all urls begin with /account (/eshop/urls.py (19line) path('account/'...)
urlpatterns = [

    path('register', views.register, name='register'), #account/register --> http resronse(views.py) - Account url setup!





]