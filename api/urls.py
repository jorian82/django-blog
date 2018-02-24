from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name="hello"),
    url(r'^time/', views.time, name="time"),
    url(r'^whosthere/', views.whosthere, name="whosthere"),
]
