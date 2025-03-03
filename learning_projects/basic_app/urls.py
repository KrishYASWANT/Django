from django.urls import path,include
from basic_app import views

# TEMPLATES URLS
app_name = 'basic_app'

urlpatterns = [
    path('registed/', views.registed, name='registration'),
]
