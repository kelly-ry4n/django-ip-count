from django.shortcuts import render
from count.models import Visitor
from count.utils import get_request_ip
from django.utils import timezone

# Create your views here.

def index(request):

    ip = get_request_ip(request)

    default_visitor_vals = {
            'last_visit': timezone.now(),
            'count':0,
    }

    visitor, _ = Visitor.objects.get_or_create(ip=ip, defaults=default_visitor_vals)
    visitor.count += 1
    visitor.update_to_now()
    visitor.save()

    ctx = {
            'ip_addr': ip,
            'visitor': visitor,
    }

    return render(request, 'index.html', ctx)

