from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Location


@login_required(login_url='/srac/login/')
def checklist(request, location_hash):
    location = get_object_or_404(Location, pk=location_hash)
    return HttpResponse('Logged in user: {}'.format(request.user))
