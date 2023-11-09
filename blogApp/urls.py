from django.urls import path
from .views import BlogPostListView

urlpatterns = [
    path('blogs/', BlogPostListView.as_view(), name='blogs'),
]
