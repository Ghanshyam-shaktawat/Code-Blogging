from django.urls import path, include
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
    path('new_post', views.new_post, name='new-post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_bookmarks/', views.my_bookmarks, name='bookmarks'),
    path('search/', views.search, name='search'),
    path('<slug:profile>/', views.profile, name='profile'),
    path('<slug:author>/<slug:slug>/', views.detail_post, name='detail'),
    path('<slug:author>/<slug:slug>/', 
        include(
            [
                path('edit', views.edit_post, name='edit-post'),
                path('delete-confirm', views.delete_post, name='delete-post'),
                path('comment', views.comments, name='comment'),
                path('like', views.like_view, name='like_post'),
                path('bookmark', views.bookmark_view, name='bookmark_post'),
            ]
        ),
    ),
]