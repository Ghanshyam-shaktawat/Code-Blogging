from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_post', views.new_post, name='new-post'),
    path('search/', views.search, name='search'),
    path('<slug:profile>/', views.profile, name='profile'),
    path('<slug:author>/<slug:slug>/', views.detail_post, name='detail'),
]