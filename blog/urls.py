from . import views
from django.urls import path
from .views import add_post

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', add_post, name='add_post'),
]