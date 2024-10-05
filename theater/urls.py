from django.urls import path, include
from rest_framework import routers

from theater.views import (
    GenreViewSet,
    ActorViewSet,
    PlayViewSet,
)


router = routers.DefaultRouter()
router.register("genres", GenreViewSet, basename="genres")
router.register("actors", ActorViewSet, basename="actors")
router.register("plays", PlayViewSet, basename="plays")

urlpatterns = [
    path("", include(router.urls))
]

app_name = "theater"
