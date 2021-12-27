from django.urls import path
from posts import views


urlpatterns = [
    path('posts/', views.PostsList.as_view, name='posts_list'),
    path('category/', views.PostsCategory.as_view, name='post_category'),
    path('search/', views.PostsSearch.as_view, name='post_search'),
    path('posts/<int:pk>', views.PostsDetails.as_view, name='post_detail'),
]