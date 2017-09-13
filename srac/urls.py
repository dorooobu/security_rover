from django.conf.urls import include, url

from . import views

app_name = 'srac'
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^checklists/(?P<location_hash>[A-Za-z0-9_]+)/', views.checklist, name='checklists'),
]