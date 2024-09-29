"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
 
from note.views import *
 
urlpatterns = [
    path('login/' , login_page, name='login'),
    path('register/', register_page, name='register'),
    path('custom_logout/' ,custom_logout, name='logout'),
    path('', editor, name='editor'),
    path('delete_note/<int:docid>/', delete_note, name='delete_note'),
    path('admin/', admin.site.urls),
]
