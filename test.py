from AOP.models import Client
import os
import django

clients = [
    Client(
        surname="Иванов",
        name="Иван",
        patronymic="Иванович",
        passport ="1234 567890",
        address="г. Москва, ул. Пушкина, д. 10",
        email="ivanov@example.com",
        phone="+7-999-123-45-67"
    ),
    Client(
        surname="Петров",
        name="Петр",
        patronymic="Петрович",
        passport ="1234 567890",
        address="г. Москва, ул. Пушкина, д. 10",
        email="ivanov@example.com",
        phone="+7-999-123-45-67"
    ),
    Client(
        surname="Николаев",
        name="Николай",
        patronymic="Николаевич",
        passport ="1234 567890",
        address="г. Москва, ул. Пушкина, д. 10",
        email="ivanov@example.com",
        phone="+7-999-123-45-67"
    ),
    Client(
        surname="Андреев",
        name="Андрей",
        patronymic="Андреевич",
        passport ="1234 567890",
        address="г. Москва, ул. Пушкина, д. 10",
        email="ivanov@example.com",
        phone="+7-999-123-45-67"
    ),
    Client(
        surname="Александров",
        name="Александр",
        patronymic="Александрович",
        passport ="1234 567890",
        address="г. Москва, ул. Пушкина, д. 10",
        email="ivanov@example.com",
        phone="+7-999-123-45-67"
    ),
]

Client.objects.bulk_create(clients)

Client.objects.filter(client_id__gt=4) 

c = Client.objects.filter(client_id=4)
c.delete()

a = Client.objects.get(pk=1)
a.name = "Игорь"
a.save()