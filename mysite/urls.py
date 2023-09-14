"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('index', views.index, name="index"),
    path('view_calories', views.view_calories, name="view_calories"),
    path('update_kcal/<request_ID>', views.update_kcal, name="update_kcal"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('view_food', views.food, name="food"),
    path('add_food', views.add_food, name="add_food"),
    path('add_kcal', views.add_kcal, name="add_kcal"),
    path('delete_food/<request_ID>', views.delete_food, name="delete_food"),
    path('edit_food/<request_ID>', views.edit_food, name="edit_food"),
    path('logins', views.logins, name="logins"),
    path('registers', views.registers, name="registers"),
    path('logouts', views.logouts, name="logouts"),
    
]
