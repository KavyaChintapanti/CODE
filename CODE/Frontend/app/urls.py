from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('upload',views.upload,name='upload'),
    path('result', views.result,name='result')

]