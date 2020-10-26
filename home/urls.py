from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('getprofile', views.getprofile, name='getprofile'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path("properties",include('properties.urls')),
    


]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    