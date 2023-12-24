from django.shortcuts import render
from .models import Participant, Lecturer, UserMaster, Course, RoomResource

def display_database(request):
    participants = Participant.objects.all()
    lecturers = Lecturer.objects.all()
    usermasters = UserMaster.objects.all()
    courses = Course.objects.all()
    roomresources = RoomResource.objects.all()
    context = {
        'participants': participants,
        'lecturers': lecturers,
        'usermasters': usermasters,
        'courses': courses,
        'roomresources': roomresources
    }
    return render(request, 'display_database.html', context)
