"""cemalproje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from ilkUygulama import views

urlpatterns = [
    url(r'^$',views.AnasayfaSayfaGorunumu.as_view()),
    url(r'^belgeler/$',views.BelgelerSayfaGorunumu.as_view()),
    url(r'^detayyenibilgim1/$',views.Detayyenibilgim1SayfaGorunumu.as_view()),
    url(r'^detayyenibilgim2/$',views.Detayyenibilgim2SayfaGorunumu.as_view()),
    url(r'^guzelsozler/$',views.GuzelsozlerSayfaGorunumu.as_view()),
    url(r'^kisabilgiler/$',views.KisabilgilerSayfaGorunumu.as_view()),
    url(r'^makaleler/$',views.MakalelerSayfaGorunumu.as_view()),
    url(r'^resimler/$',views.ResimlerSayfaGorunumu.as_view()),
    url(r'^anasayfa/$',views.AnasayfaSayfaGorunumu.as_view()),
]
