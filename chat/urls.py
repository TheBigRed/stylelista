from django.urls import path, re_path
from . import views


app_name = 'chat'
urlpatterns = [
    path('', views.messages, name='messages')
]
