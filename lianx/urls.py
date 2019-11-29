"""lianx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app_two import views
from app import views as ti
from lianx import views as vi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('job/', include('app_two.urls')),
    path('login/', vi.login),
    path('zong/', vi.zong),
    path('test/', vi.text),
    path('zong/', include('app.urls')),
    path('data/', vi.data),
    path("gouwuche/", vi.gouwuche),
    # path("one/", vi.two),
    # path('two/', vi.theee),
    path('Cart/', include('app.urls')),
    path('paging/', include('app.urls')),
]
