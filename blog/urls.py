from . import views
from django.urls import path
from .views import PostList, PostDetail, AddPost, DeletePostView, UserProfileView

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("add_post/", AddPost.as_view(), name="add_post"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete/<int:pk>/remove/', DeletePostView.as_view(), name='delete_post'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('user/<str:username>/', UserProfileView.as_view(), name='user_profile'),
]