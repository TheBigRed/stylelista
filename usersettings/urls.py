from django.urls import path
from . import views


app_name = 'usersettings'
urlpatterns = [
    path('', views.index, name='index'),
    path('updateaccount/', views.updateaccount, name='updateaccount'),
    path('upload/', views.img_upload, name='img_upload'),
]
