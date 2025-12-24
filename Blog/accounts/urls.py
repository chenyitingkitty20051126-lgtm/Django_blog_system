from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # 包含 Django 默认的登录/注销页面 (login, logout)
    path('', include('django.contrib.auth.urls')),
    # 注册页面的路由
    path('register/', views.register, name='register'),
]