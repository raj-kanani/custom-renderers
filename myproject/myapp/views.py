from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .renderers import *


# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    renderer_classes = [CustomRenderers]


#
# class UserCountView(APIView):
#     """
#     A view that returns the count of active users in JSON.
#     """
#     renderer_classes = [JSONRenderer]
#
#     def get(self, request, format=None):
#         name_count = Image.objects.filter(status=True).count()
#         content = {'name_count': name_count}
#         return Response(content)

from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCountView(APIView):
    """
    A view that returns the count of active users in JSON.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = User.objects.filter(is_active=True).count()
        content = {'user_count': user_count}
        return Response(content)

