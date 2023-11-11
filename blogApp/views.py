from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
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


class AddBlogPost(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogPostSerializer

    def post(self, request):
        user = self.request.user
        if 'title' in request.data and 'content' in request.data:  # Assuming 'title' and 'content' are sent from the frontend
            title = request.data['title']
            content = request.data['content']

            # Perform actions with the received data
            # For example, creating a new BlogPost instance
            new_post = BlogPost.objects.create(title=title, content=content, author=user)

            # You might also use a serializer to handle creating the object
            
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({'message': 'Blog Post Created'}, status=status.HTTP_201_CREATED)

        # Return an error response with status code 400 if data is incomplete
        return Response({'error': 'Incomplete data received'}, status=status.HTTP_400_BAD_REQUEST)