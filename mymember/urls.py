from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member_list/', views.member_list, name='member_list'),
    path('register/', views.register, name='register'),
    path('complete/', views.complete, name='complete'),

]
