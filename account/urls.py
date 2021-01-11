from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'account'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('dashboard/', views.dashboard, name='dashboard'),

]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
