from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import Category
from .serializers import (CategorySerializer,)
from . import services
from rest_framework.exceptions import NotFound


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer

    def get_object(self, *args, **kwargs):
        try:
            category = Category.objects.get(id=kwargs['pk'])
        except Exception as e:
            raise NotFound('category not found')
        return category

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs and kwargs["pk"]:
            return Response(services.get_category_by_id(kwargs['pk']), status=status.HTTP_200_OK)
        else:
            return Response(services.get_all_categories(), status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object(*args, **kwargs)
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object(*args, **kwargs)
        instance.delete()
        return Response({"success": True}, status=status.HTTP_200_OK)
