
from django.contrib import admin
from django.urls import path, include

from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("todo.urls")),
    path("", health_check),  # 👈 Tohle je důležité!
]