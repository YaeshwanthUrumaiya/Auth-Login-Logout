from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('login', views.login),
    re_path('signin', views.signin),
    re_path('test', views.test),
    re_path('logout', views.logout),
    re_path('fetch_user', views.fetch_user_data),
]
