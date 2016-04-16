from django.shortcuts import render
from count.models import Visitor

# Create your views here.

def index(request):

    ctx = {
            'ip_addr':'192.168.1.1',
            'num_visits':10,
            
    }

    return render(request, 'index.html', ctx)
