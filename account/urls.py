from django.urls import path

from . import views

#all urls begin with /account (/eshop/urls.py (19line) path('account/'...)
urlpatterns = [

    path('register', views.register, name='register'), #account/register --> http resronse(views.py) - Account url setup!

    #Email verification URL's
    path('email_verification', views.email_verification, name='email-verification'),

    path('email_verification-sent', views.email_verification_sent, name='email-verification-sent'),

    path('email_verification-success', views.email_verification_success, name='email-verification-success'),

    path('email_verification-failed', views.email_verification_failed, name='email-verification-failed'),

]