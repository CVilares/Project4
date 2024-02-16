from . import views
from django.urls import path
from .views import PostList, PostDetail, AddPost

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    
]