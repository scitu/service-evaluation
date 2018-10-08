"""service_evaluation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, reverse
from django.contrib.auth.views import logout_then_login
from app.views import evaluation, evaluation_with_service, index
from app.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('logout/', logout_then_login, name="logout"),
    path('eval/<slug:service>', evaluation_with_service, name="evaluation-with-service"),
    path('eval/', evaluation, name="evaluation"),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/', include(router.urls)),
]