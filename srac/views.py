from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import reverse
from django.utils import timezone
from datetime import timedelta

from .models import Location
from .models import Location_Checklist
from .models import Session
from .models import Session_Checklist


@login_required(login_url='/srac/login/')
def checklist(request, location_hash):
    # first, check if location_hash is valid
    location = get_object_or_404(Location, pk=location_hash)

    existing_session_set = Session.objects.filter(is_session_submitted=0)
    if len(existing_session_set) == 0:
        print("There are NO existing sessions")

        # check for sessions completed an hour ago
        now = timezone.now()
        one_hour_ago = now - timedelta(hours=1)
        earlier_sessions_list = Session.objects.filter(check_date__range=(one_hour_ago, now)).filter(is_session_submitted=1)

        if len(earlier_sessions_list) > 0:
            for earlier_session in earlier_sessions_list:
                print("Earlier session: {}".format(earlier_session.session_id))
                session_checklist_set = Session_Checklist.objects.filter(session=earlier_session)
                for session_checklist in session_checklist_set:
                    if session_checklist.location_checklist.location == location:
                        context = {
                            'prompt': "recent",
                            'location': location,
                            'session': earlier_session
                        }
                        return render(request, 'srac/checklist_prompt.html', context)

        return HttpResponseRedirect(
            reverse('srac:session.add', kwargs={'location_hash': location_hash})
        )
    else:
        print("There are existing sessions")
        # check if there is an existing session in the location
        for existing_session in existing_session_set:
            for session_checklist in existing_session.session_checklist_set.all():
                if session_checklist.location_checklist.location == location:
                    print("There is an existing session for {}: {}".format(location, existing_session.session_id))
                    context = {
                        'prompt': "exist",
                        'location': location,
                        'session': existing_session
                    }
                    return render(request, 'srac/checklist_prompt.html', context)


def session_add(request, location_hash):
    current_user = get_object_or_404(User, pk=request.user.id)
    location = get_object_or_404(Location, pk=location_hash)

    context = {
        'user': current_user,
    }

    session = Session(
        check_date=timezone.now(),
        checker=current_user
    )
    session.save()
    context['session'] = session

    location_checklists_set = Location_Checklist.objects.filter(location=location)
    for location_checklist in location_checklists_set:
        session.session_checklist_set.create(
            session=session,
            location_checklist=location_checklist
        )

    session_checklist_set = session.session_checklist_set.all()
    context['checklist_set'] = session_checklist_set

    return render(request, 'srac/checklist.html', context)


def session_edit(request, session_id):
    current_user = get_object_or_404(User, pk=request.user.id)

    context = {
        'user': current_user,
    }

    session = Session.objects.get(pk=session_id)
    context['session'] = session

    context['checklist_set'] = session.session_checklist_set.all()

    return render(request, 'srac/checklist.html', context)


def session_save(request, session_id):
    if request.method == 'POST':
        session = Session.objects.get(pk=session_id)

        # save changes
        for session_checklist in session.session_checklist_set.all():
            session_checklist.confirmation = request.POST['confirmation_' + str(session_checklist.session_checklist_id)]
            session_checklist.remarks = request.POST['remarks_' + str(session_checklist.session_checklist_id)]
            session_checklist.save()

        session.check_remarks = request.POST['session_remarks']
        session.check_date = timezone.now()
        session.is_session_submitted = 1
        session.save()

        return HttpResponseRedirect(
            reverse('srac:session.view', kwargs={'session_id': session.session_id}) + "?success=true"
        )


def session_view(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    context = {
        "checklist_set": session.session_checklist_set.all(),
        "session": session
    }
    if "success" in request.GET:
        context["success"] = "true"

    return render(request, 'srac/checklist_view.html', context)
