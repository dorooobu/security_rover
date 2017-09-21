from django.conf.urls import include, url

from . import views

app_name = 'srac'
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^checklists/(?P<location_hash>[A-Za-z0-9_]+)', views.checklist, name='checklists'),
    url(r'^session/add/(?P<location_hash>[A-Za-z0-9_]+)', views.session_add, name='session.add'),
    url(r'^session/edit/(?P<session_id>[0-9_]+)', views.session_edit, name='session.edit'),
    url(r'^session/save/(?P<session_id>[0-9_]+)', views.session_save, name='session.save'),
    url(r'^session/view/(?P<session_id>[0-9_]+)', views.session_view, name='session.view'),
]