from django.urls import path, include
from rest_framework import routers

from theater.views import GenreViewSet


router = routers.DefaultRouter()
router.register("genres", GenreViewSet, basename="genres")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "theater"
