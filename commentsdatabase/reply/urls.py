from django.urls import path, include
from django.urls.resolvers import URLPattern 
from . import views
from django.contrib import admin

urlpatterns = [
    path('reply/',views.ReplyList.as_view()),
    path('reply/<int:pk>/', views.ReplyDetail.as_view()),
]