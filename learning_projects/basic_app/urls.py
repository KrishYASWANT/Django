from django.urls import path,include
from basic_app import views

# TEMPLATES URLS
app_name = 'basic_app'

urlpatterns = [
    path('registed/', views.registed, name='registration'),
    path('welcome/', views.welcome, name = 'welcome'),
    path('user_login/', views.user_login, name='user_login'),
    path('update_profile_pic/', views.update_profile_pic, name='update_profile_pic'),
]
