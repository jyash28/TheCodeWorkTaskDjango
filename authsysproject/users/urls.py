from allauth.account.views import SignupView
from django.contrib.auth import views as auth_view
from django.urls import path, include

from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('accounts/', include('allauth.urls')),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    # path('two-factor/', two_factor_login_view, name='two_factor_login'),
    # path('login/', auth_views.LoginView.as_view(
    #         authentication_form=OTPAuthenticationForm, template_name='users/login.html'), name='login'),
]
