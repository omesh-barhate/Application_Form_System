"""form_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from form_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name="main"),
    path('register',views.register,name="register"),
    path('home',views.dashboard,name="home"),
    path('bms_home',views.bms_home,name="bms-home"),
    path('form',views.basic_form,name="form"),
    path('doLogin',views.doLogin),
    path('register_save',views.register_save,name="user_registration"),
    path('register_check',views.register_check,name="register_check"),
    path('test',views.test,name="test")
]