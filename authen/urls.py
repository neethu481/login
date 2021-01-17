from django.urls import path
from . import views

app_name = 'authen'

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('landing', views.landing_view, name='landing'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dropdown/', views.dropdown_view, name='dropdown')
]