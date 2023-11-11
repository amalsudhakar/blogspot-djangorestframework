from django.urls import path
from .views import BlogPostListView, AddBlogPost

urlpatterns = [
    path('blogs/', BlogPostListView.as_view(), name='blogs'),
    path('create-blog/', AddBlogPost.as_view(), name='blog_post'),
]
