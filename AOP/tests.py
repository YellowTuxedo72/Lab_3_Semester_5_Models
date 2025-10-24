from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from AOP.models import Client

def create_client(surname, name):
    return Client.objects.create(
        surname=surname,
        name=name,
        patronymic="Тестович",
        passport="1234 567890",
        address="г. Тест, ул. Тестова",
        email= "lolkek@gmail.com",
        phone="+7-996-313-46-94"
    )


class ClientListViewTests(TestCase):
    def test_no_clients(self):
        response = self.client.get(reverse("AOP:clients"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Клиенты отсутствуют")
        self.assertQuerySetEqual(response.context["clients"], [])

    def test_one_client(self):
        client = create_client("Иванов", "Иван")
        response = self.client.get(reverse("AOP:clients"))
        self.assertQuerySetEqual(response.context["clients"], [client])
        self.assertContains(response, "Иван")

    def test_multiple_clients(self):
        client1 = create_client("Петров", "Пётр")
        client2 = create_client("Сидоров", "Сидор")
        response = self.client.get(reverse("AOP:clients"))
        self.assertQuerySetEqual(
            response.context["clients"],
            [client1, client2],
            ordered=False
        )

# Create your tests here.
