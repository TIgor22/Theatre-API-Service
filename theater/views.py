from rest_framework import viewsets

from theater.models import (
    Genre,
    Actor,
)
from theater.serializers import (
    GenreSerializer,
    ActorSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
