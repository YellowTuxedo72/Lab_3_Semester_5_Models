from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from AOP.models import Client, ClientContract, Services, Suppliers, ProvidedServices, ContractDetails
from datetime import date


# Вспомогнательные функции 
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

def create_contract(client, number):
    return ClientContract.objects.create(
        client_id=client,
        contract_number=number,
        signing_date=date.today(),
        signing_place="г. Тест",
        expiration_date=date.today(),
        total_amount=1000
    )
def create_supplier(name):
    return Suppliers.objects.create(
        name=name,
        inn="123456789012",
        address="г. Тест, ул. Тестова",
        email="lolkek@gmail.com",
        phone="+7-996-313-46-94"
    )

def create_service(name):
    return Services.objects.create(
        name=name,
        description="Описание услуги"
    )
    
def create_provided_service(service, supplier, cost):
    return ProvidedServices.objects.create(
        service_id=service,
        supplier_id=supplier,
        service_cost=cost
    )

def create_contract_detail(contract, provided_service, quantity):
    return ContractDetails.objects.create(
        contract=contract,
        provided_service_id=provided_service,
        quantity=quantity,
        service_date=date.today()
    )
    
#Тесты
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

    def test_few_clients(self):
        client1 = create_client("Петров", "Пётр")
        client2 = create_client("Сидоров", "Сидор")
        response = self.client.get(reverse("AOP:clients"))
        self.assertQuerySetEqual(response.context["clients"], [client1, client2], ordered=False)

class ClientContractListViewTests(TestCase):
    def test_no_contracts(self):
        response = self.client.get(reverse("AOP:clientContracts"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Договоров нет")
        self.assertQuerySetEqual(response.context["contracts"], [])

    def test_one_contract(self):
        client = create_client("Иванов", "Иван")
        contract = create_contract(client, 1)
        response = self.client.get(reverse("AOP:clientContracts"))
        self.assertQuerySetEqual(response.context["contracts"], [contract])
        self.assertContains(response, contract.client_id.name)

    def test_few_contracts(self):
        client1 = create_client("Иванов", "Иван")
        client2 = create_client("Петров", "Пётр")
        contract1 = create_contract(client1, 1)
        contract2 = create_contract(client2, 2)
        response = self.client.get(reverse("AOP:clientContracts"))
        self.assertQuerySetEqual(response.context["contracts"], [contract1, contract2], ordered=False)

class SuppliersTests(TestCase):
    def test_no_suppliers(self):
        response = self.client.get(reverse("AOP:suppliers"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Подрядчиков нет")
        self.assertQuerySetEqual(response.context["suppliers"], [])

    def test_one_supplier(self):
        supplier = create_supplier("Подрядчик")
        response = self.client.get(reverse("AOP:suppliers"))
        self.assertQuerySetEqual(response.context["suppliers"], [supplier])
        self.assertContains(response, "Подрядчик")

    def test_few_suppliers(self):
        supplier1 = create_supplier("Подрядчик 1")
        supplier2 = create_supplier("Подрядчик 2")
        response = self.client.get(reverse("AOP:suppliers"))
        self.assertQuerySetEqual(
            response.context["suppliers"],
            [supplier1, supplier2],
            ordered=False
        )

class ServicesViewTests(TestCase):
    def test_no_services(self):
        response = self.client.get(reverse("AOP:services"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Услуг нет")
        self.assertQuerySetEqual(response.context["services"], [])

    def test_one_service(self):
        service = create_service("Предоставляемая услуга")
        response = self.client.get(reverse("AOP:services"))
        self.assertQuerySetEqual(response.context["services"], [service])
        self.assertContains(response, "Предоставляемая услуга")

    def test_few_services(self):
        service1 = create_service("услуга 1")
        service2 = create_service("услуга 2")
        response = self.client.get(reverse("AOP:services"))
        self.assertQuerySetEqual(
            response.context["services"],
            [service1, service2],
            ordered=False
        )
        
class ProvidedServicesViewTests(TestCase):
    def test_no_provided_services(self):
        response = self.client.get(reverse("AOP:providedServices"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Предоставляемых услуг нет")
        self.assertQuerySetEqual(response.context["services"], [])

    def test_one_provided_service(self):
        service = create_service("предоставляемая услуга 1")
        supplier = create_supplier("подрядчик 1")
        provided = create_provided_service(service, supplier, 1000)
        response = self.client.get(reverse("AOP:providedServices"))
        self.assertQuerySetEqual(response.context["services"], [provided])

    def test_few_provided_services(self):
        service1 = create_service("услуга 1")
        supplier1 = create_supplier("подрядчик 1")
        provide1 = create_provided_service(service1, supplier1, 500)
        service2 = create_service("услуга 2")
        supplier2 = create_supplier("подрядчик 2")
        provide2 = create_provided_service(service2, supplier2, 1000)
        response = self.client.get(reverse("AOP:providedServices"))
        self.assertQuerySetEqual(
            response.context["services"],
            [provide1, provide2],
            ordered=False
        )
        
class ContractDetailsViewTests(TestCase):
    def test_no_details(self):
        response = self.client.get(reverse("AOP:contractDetails"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Деталей договоров нет")
        self.assertQuerySetEqual(response.context["details"], [])

    def test_one_detail(self):
        client = create_client("Иванов", "Иван")
        contract = create_contract(client, 1)
        service = create_service("услуга 1")
        supplier = create_supplier("подрядчик 1")
        provided = create_provided_service(service, supplier, 1000)
        detail = create_contract_detail(contract, provided, 2)
        response = self.client.get(reverse("AOP:contractDetails"))
        self.assertQuerySetEqual(response.context["details"], [detail])

    def test_few_details(self):
        client = create_client("Петров", "Пётр")
        contract = create_contract(client, 1)
        service1 = create_service("услуга 1")
        supplier1 = create_supplier("подрядчик 1")
        provide1 = create_provided_service(service1, supplier1, 500)
        service2 = create_service("услуга 2")
        supplier2 = create_supplier("подрядчик 2")
        provide2 = create_provided_service(service2, supplier2, 1000)
        detail1 = create_contract_detail(contract, provide1, 2)
        detail2 = create_contract_detail(contract, provide2, 3)
        response = self.client.get(reverse("AOP:contractDetails"))
        self.assertQuerySetEqual(
            response.context["details"],
            [detail1, detail2],
            ordered=False
        )