from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post', views.new_post, name='new-post'),
    path('search/', views.search, name='search'),
    path('<slug:slug>/', views.detail_post, name='detail'),
]