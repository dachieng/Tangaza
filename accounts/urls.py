from django.urls import path

from django.conf.urls import url

from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
   url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
]