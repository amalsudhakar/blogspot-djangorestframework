from django.views.generic import TemplateView
from rest_framework.generics import ListAPIView
from .serializers import BlogPostSerializer
from .models import BlogPost
from rest_framework.permissions import AllowAny

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]
