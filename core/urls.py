from django.urls import path, include
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
    path('new/', views.new_post, name='new_post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('bookmarks/', views.my_bookmarks, name='bookmarks'),
    path('search/', views.search, name='search'),
    path('category/<str:cat>/', views.category_view, name='category'),
    path('like/<int:post_id>/', views.like_view, name='like_post'),
    path('bookmark/<int:post_id>/', views.bookmark_view, name='bookmark_post'),
    path('<slug:profile>/', views.profile, name='profile'),
    path('<slug:author>/<slug:slug>/', views.detail_post, name='detail'),
    path('<slug:author>/<slug:slug>/', 
        include(
            [
                path('edit', views.edit_post, name='edit_post'),
                path('delete-confirm', views.delete_post, name='delete_post'),
                path('comment', views.comments, name='comment'),
            ]
        ),
    ),
]