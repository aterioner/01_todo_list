from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-created")
    serializer_class = TaskSerializer

    def list(self, request, *args, **kwargs):
        print("📥 GET request headers:", dict(request.headers))
        print("📥 GET request content type:", request.content_type)
        print("📥 GET request accepted:", request.accepted_media_type)
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print("📤 POST data:", request.data)
        return super().create(request, *args, **kwargs)
    
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def test_api(request):
    return Response({"message": "API is working!"})