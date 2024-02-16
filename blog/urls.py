from . import views
from django.urls import path
from .views import PostList, PostDetail, NewPost

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("new_post/", NewPost.as_view(), name="new_post"),
]