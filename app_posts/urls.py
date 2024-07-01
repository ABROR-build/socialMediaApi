from django.urls import path
from . import views

urlpatterns = [
    # posts
    path('all_posts/', views.ListPosts.as_view(), name='list-posts'),
    path('post/<int:pk>/', views.PostDeatil.as_view(), name='post-detail'),
    path('create_post/', views.PostsCreate.as_view(), name='post-create'),
    path('update_post/<int:pk>/', views.PutPost.as_view(), name='post-put'),
    path('delete_post/<int:pk>/', views.PostsDelete.as_view(), name='post-delete'),

    # comments
    path('comments/<int:pk>/', views.ListComments.as_view(), name='list-comments'),  # pk - postning pk
    path('create_comment/<int:pk>/', views.CreateComment.as_view(), name='create-comment'),
    path('update_comment/<int:pk>/', views.PutComment.as_view(), name='update-comment')

]
