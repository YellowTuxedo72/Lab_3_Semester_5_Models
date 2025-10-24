from django.urls import path

from . import views

app_name = "AOP"

urlpatterns = [
    path("clients/", views.client, name="clients"),
    path("clientContract/", views.clientContract, name='clientContracts')
]