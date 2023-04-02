from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>', views.PostDetailView.as_view(), name='detail')
    # path('<int:post_id>', views.detailPost, name='detailPost'),
    # path('newpost/', views.newPost, name='newpost')
]