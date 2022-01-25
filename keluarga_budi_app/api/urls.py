from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('list/', views.personList, name='person-list'),
    path('create/', views.personCreate, name='person-create'),
    path('detail/<str:pk>/', views.personDetail, name='person-detail'),
    path('update/<str:pk>/', views.personUpdate, name='person-update'),
    path('delete/<str:pk>/', views.personDelete, name='person-delete'),
]