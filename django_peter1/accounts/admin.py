from django.contrib import admin
from .models import Participant, Lecturer


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    ...
    # ... configuration for Participant admin


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    ...
    # ... configuration for Lecturer admin
