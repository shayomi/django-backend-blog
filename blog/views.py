from django.shortcuts import render
from .serializer import (Blog, BlogComment, BlogTag,
                        BlogSerializer, BlogTagSerializer,
                        BlogCommentSerializer)
from .models import BlogTag, BlogComment, Blog
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class BlogView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "slug"

class BlogCommentView(ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

    def get_queryset(self):
        query = self.request.query_params.dict()

        return self.queryset.filter(**query)


class BlogTagView(ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer
