from django.contrib import admin

from .models import Checklist
from .models import Classification
from .models import Location

admin.site.register(Checklist)
admin.site.register(Classification)
admin.site.register(Location)