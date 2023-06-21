from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('users/', views.user_list, name='user_list'),
    path('users/<username>', views.detail, name='user_detail'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
