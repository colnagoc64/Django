"""djangoProject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import djangoProject4.views
import member.views
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',djangoProject4.views.index),
    path('start/',member.views.start ),
    path('start2/',board.views.start2),
    path('start3/',board.views.start3),
    path('start4',board.views.start4),
    # post방식은 / 붙이면안됨
    path('app1', include('app1.urls')),

]
