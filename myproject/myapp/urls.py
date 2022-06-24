from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('student', views.StudentView, basename='myapi')

urlpatterns = [
        path('', include(router.urls)),
        path('__debug__/', include('debug_toolbar.urls')),
        # path('image/', views.UserCountView.as_view)
]
