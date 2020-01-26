"""brc_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gear/', include('gear.urls')),
    path('homework/', include('homework.urls')),
    path('meetings/', include('meetings.urls')),
    path('posts/', include('posts.urls')),
]

# from rest_framework import routers

# from gear import views as gear_views
#from homework import views as homework_views

# router = routers.DefaultRouter()
# router.register(r'gear', gear_views.GearView, 'gear')
#router.register(r'homework', homework_views.HomeworkView, 'homework')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
# ]
