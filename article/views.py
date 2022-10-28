from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from article import serializers
import article
from article.models import Articles
from article.serializers import ArticlesSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404


# Create your views here.

class articleslist(APIView):
    def get(self, request, format=None):
        articles=Articles.objects.all()
        Serializer=ArticlesSerializer(articles, many=True)
        return Response(Serializer.data)

    def post(self, request, format=None):
        Serializer = ArticlesSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data,status=status.HTTP_201_CREATED)
        else:
            print(Serializer.errors)
            return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)