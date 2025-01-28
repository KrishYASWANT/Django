#from django.conf.urls import url
from django.urls import path
from basic_app import views # we can use . for currect location in place of basic_app


# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('others/', views.others, name='others'),
    
]
