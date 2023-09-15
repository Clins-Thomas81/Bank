from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('new', views.new, name='new'),
    path('form', views.form, name='form'),
    path('accept', views.accept, name='accept'),
]
