from django.shortcuts import render
from .models import Client, ClientContract

def client(request):
    clients = Client.objects.all()
    return render(request, 'AOP/clients.html', {'clients':clients})
# Create your views here.


def clientContract(request):
    contracts = ClientContract.objects.select_related('client_id').all()
    return render(request, 'AOP/clientContracts.html', {'contracts': contracts})
    