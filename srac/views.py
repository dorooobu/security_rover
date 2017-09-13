from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone

from .models import Location_Checklist
from .models import Session
from .models import Session_Checklist


@login_required(login_url='/srac/login/')
def checklist(request, location_hash):
    current_user = get_object_or_404(User, pk=request.user.id)

    if request.method == 'POST':
        pass
    else:
        context = {
            'location_hash': location_hash
        }
        session_checklist_set = None

        existing_session_set = Session.objects.filter(is_session_submitted=0)
        if len(existing_session_set) == 0:
            print("There are NO existing sessions")
            session = Session(
                check_date=timezone.now(),
                checker=current_user
            )
            session.save()

            location_checklists_set = Location_Checklist.objects.filter(location=location_hash)
            for checklist in location_checklists_set:
                session.session_checklist_set.create(
                    session=session,
                    location_checklist=checklist
                )

            session_checklist_set = Session_Checklist.objects.filter(session=session)
        else:
            print("There are existing sessions")
            # check if there is an existing session in the location
            session_checklist_set = None
            for existing_session in existing_session_set:
                session_checklist_set = Session_Checklist.objects.filter(session=existing_session)
                for session_checklist in session_checklist_set:
                    if session_checklist.location_checklist.location.location_hash == location_hash:
                        print("There is an existing session for this location: {}".format(location_hash))
                        break

        context['checklist_set'] = session_checklist_set
        return render(request, 'srac/checklist.html', context)
