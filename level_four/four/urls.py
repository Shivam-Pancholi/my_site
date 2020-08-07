from django.urls import path
from . import views

app_name = 'four'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('another/', views.another, name='another'),
    path('form/', views.form_view, name='form'),
    path('user_login', views.user_login, name='login')
]
