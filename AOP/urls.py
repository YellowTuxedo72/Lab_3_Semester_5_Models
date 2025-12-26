from django.urls import path

from . import views

app_name = "AOP"

urlpatterns = [
    path("clients/", views.client, name="clients"),
    path("clientContract/", views.clientContract, name='clientContracts'),
    path("services/", views.services, name="services"),
    path("suppliers/", views.suppliers, name="suppliers"),
    path("providedServices/", views.provided_services, name="providedServices"),
    path("contractDetails/", views.contract_details, name="contractDetails"),
]