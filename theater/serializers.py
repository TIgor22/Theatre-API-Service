from rest_framework import serializers

from theater.models import (
    Genre,
    Actor,
    Play,
    TheatreHall,
    Performance,
    Ticket,
    Reservation
)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")
