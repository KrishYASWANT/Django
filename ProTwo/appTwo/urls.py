#from django.conf.urls import url
from appTwo import views
from django.urls import path

urlpatterns = [
    path('', views.users, name='users')
]
