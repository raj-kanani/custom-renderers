from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from .renderers import *


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    renderer_classes = [CustomRenderer1]
    # renderer_classes = [custom_exception]

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


# class UserCountView(APIView):
#     """
#     A view that returns the count of active users in JSON.
#     """
#     renderer_classes = [CustomJSONRenderer]
#
#     def get(self, request, format=None):
#         user_count = User.objects.filter(is_active=True).count()
#         content = {'user_count': user_count}
#         return Response(content)
#     # def get(self, request, format=None):
#     #     stu = Student.objects.all()
#     #     serializer = StudentSerializer(stu, many=True)
#     #     return Response(serializer.data)
