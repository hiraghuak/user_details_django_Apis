from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import fetchAPi, ListChildView, ListUserMasterView, UpdateUserMasterView,UpdateChildView,SomeModelCSVExportView



urlpatterns = [
    path('fetch/', fetchAPi.as_view()),
    path('child/', ListChildView.as_view()),
    path('child/<int:pk>/', UpdateChildView.as_view()),
    path('user_master/', ListUserMasterView.as_view()),
    path('user_master/<int:pk>/', UpdateUserMasterView.as_view()),   
    path('csv/', SomeModelCSVExportView.as_view()),
]
