from django.test import TestCase
from rest_framework.test import APITestCase
import json
from django.urls import reverse
from .models import Efemeride
from django.contrib.auth.models import User
import os
import random
import string
random.seed(123)


# Create your tests here.
class EfemerideListCreateAPIViewTestCase(APITestCase):
    url = "/efemerides"

    def setUp(self):
        self.username = os.environ.get("DJANGO_ADMIN_USER", "admin")
        self.email = os.environ.get("DJANGO_ADMIN_MAIL", "mario.lopez.dev@gmail.com")
        self.password = os.environ.get("DJANGO_ADMIN_PASSWORD", "marioalop789!!!")
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = self.api_authentication()

    def api_authentication(self):
        token = self.client.post("/token/", {"username": self.username, "password": self.password})
        token = token.json()
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token["access"])

    def test_list_efemeride(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_create_efemeride(self):
        response = self.client.post(self.url, {"cita": "mi cumple", "dia": "2019-05-14"})
        self.assertEqual(405, response.status_code)

    def test_list_efemeride_filter_ok(self):
        response = self.client.get("{}?day=2019-05-14".format(self.url))
        self.assertEqual(200, response.status_code)

    def test_list_efemeride_filter_bad(self):
        bad_string = ''.join(random.choice(string.ascii_uppercase +
                                           string.ascii_lowercase +
                                           string.digits)
                             for _ in range(8))
        response = self.client.get("{}?day={}".format(self.url, bad_string))
        self.assertEqual(400, response.status_code)

    def test_put_efemeride(self):
        response = self.client.post(self.url + "/1/", {"cita": "mi cumple", "dia": "2019-05-14"})
        self.assertEqual(404, response.status_code)