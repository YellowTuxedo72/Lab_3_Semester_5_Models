from django.shortcuts import render
from .models import Client, ClientContract, Services, Suppliers, ProvidedServices, ContractDetails
def client(request):
    clients = Client.objects.all()
    return render(request, 'AOP/clients.html', {'clients':clients})

def clientContract(request):
    contracts = ClientContract.objects.select_related('client_id').all()
    return render(request, 'AOP/clientContracts.html', {'contracts': contracts})
    
def services(request):
    services = Services.objects.all()
    return render(request, 'AOP/services.html', {'services': services})

def suppliers(request):
    suppliers = Suppliers.objects.all()
    return render(request, 'AOP/suppliers.html', {'suppliers': suppliers})

def provided_services(request):
    services = ProvidedServices.objects.select_related('service_id', 'supplier_id').all()
    return render(request, 'AOP/providedServices.html', {'services': services})

def contract_details(request):
    details = ContractDetails.objects.select_related(
        'contract__client_id',
        'provided_service_id__service_id',
        'provided_service_id__supplier_id'
    ).all()
    return render(request, 'AOP/contractDetails.html', {'details': details})