from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.archive),
    url(r'register/', views.register),
    url(r'login/', views.login),
    url(r'write/', views.write)
]
