from django.db import models

class Client(models.Model):
    client_id = models.AutoField(primary_key=True) 
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, null=True)
    passport = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.client_id)

class ClientContract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    contract_number = models.IntegerField()
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    signing_date = models.DateField()
    signing_place = models.CharField(max_length=100)
    expiration_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)

class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    
class Suppliers(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    inn = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=18)
    
class ProvidedServices(models.Model):
    provided_service_id = models.AutoField(primary_key=True)
    service_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    service_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    
class ContractDetails(models.Model):
    contract = models.ForeignKey(ClientContract, on_delete=models.CASCADE)
    provided_service_id = models.ForeignKey(ProvidedServices, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(null=True, blank=True)
    service_date = models.DateField()

