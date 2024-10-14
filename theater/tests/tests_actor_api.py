from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
from rest_framework import status

from theater.models import Actor
from theater.serializers import ActorSerializer


def sample_actor(**params) -> Actor:
    defaults = {
        "first_name": "Orlando",
        "last_name": "Blum"
    }
    defaults.update(params)
    return Actor.objects.create(**defaults)

def detail_url(actor_id):
    return reverse("theater:actor-detail", args=(actor_id,))

ACTOR_URL = reverse("theater:actor-list")

class UnauthenticatedActorApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(ACTOR_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedActorApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test.test",
            password="testpassword"
        )
        self.client.force_authenticate(self.user)

    def test_actors_list(self):
        sample_actor()

        res = self.client.get(ACTOR_URL)
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["results"], serializer.data)

    def test_retrieve_actor_detail(self):
        actor = sample_actor()

        url = detail_url(actor.id)
        res = self.client.get(url)
        serializer = ActorSerializer(actor)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_actor_forbidden(self):
        payload = {
            "first_name": "Harry",
            "last_name": "Potter"
        }

        res = self.client.post(ACTOR_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminActorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="admin@admin.test",
            password="testpassword",
            is_staff=True
        )
        self.client.force_authenticate(self.user)

    def test_create_actor(self):
        payload = {
            "first_name": "Harry",
            "last_name": "Potter"
        }

        res = self.client.post(ACTOR_URL, payload)
        actor = Actor.objects.get(id=res.data["id"])

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        for key in payload:
            self.assertEqual(payload[key], getattr(actor, key))
