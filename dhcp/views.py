from django.http import JsonResponse
from .models import IPAddress

# Create your views here.

def ip_address_list(request):
    ip_addresses = IPAddress.objects.values('address', 'hostname')
    return JsonResponse({'ip_addresses': list(ip_addresses)})
    
