from django.conf.urls import url

from . import views

app_name = 'srac'
urlpatterns = [
    url(r'^checklists/(?P<location_hash>[A-Za-z0-9]+)/', views.checklist, name='checklists')
]