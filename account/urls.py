from django.urls import path

from . import views 

from django.contrib.auth import views as auth_views

#all urls begin with /account (/eshop/urls.py (19line) path('account/'...)
urlpatterns = [

    path('register', views.register, name='register'), #account/register --> http resronse(views.py) - Account url setup!

    #Email verification URL's
    path('email-verification/<str:uidb64>/<str:token>/', views.email_verification, name='email-verification'),# <str:u... made our url dynamic

    path('email-verification-sent', views.email_verification_sent, name='email-verification-sent'),

    path('email-verification-success', views.email_verification_success, name='email-verification-success'),

    path('email-verification-failed', views.email_verification_failed, name='email-verification-failed'),

    # Login\Logout urls

    path('my-login', views.my_login, name='my-login'),

    path('user-logout', views.user_logout, name='user-logout'),
 
    # Dashboard / profile URLs
    path('dashboard', views.dashboard, name='dashboard'),

    path('profile-management', views.profile_management, name='profile-management'),

    path('delete-account', views.delete_account, name='delete-account'),


    #password management URLs/views

    # 1) Submit your email form
    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),

    # 2) Success message stating that a password reset was sent
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    # 3)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # 4) Success message stating that our password was reset
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    


    


]