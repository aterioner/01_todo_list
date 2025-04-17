from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, test_api

router = DefaultRouter()
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("ping/", test_api),  # nový testovací endpoint
]


