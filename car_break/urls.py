"""car_break URL Configuration

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
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('main/', views.main, name='main'),
    path('side01/', views.side01, name='side01'),
    path('side02/', views.side02, name='side02'),
    path('side03/', views.side02, name='side03'),
    path('admin01/', views.admin, name='admin01'),
    path('main01/', views.main01, name='main01'),
    path('upload/', views.upload, name='upload'),
    path('visitor/', views.visitor, name='visitor'),
    path('usage/', views.usage, name='usage'),
    path('user/', views.user, name='user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)