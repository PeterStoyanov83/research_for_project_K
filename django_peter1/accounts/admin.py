from django.contrib import admin
from .models import Participant, Lecturer, UserMaster, Course, RoomResource


class ParticipantAdmin(admin.ModelAdmin):
    def courses_attending_display(self, obj):
        return ", ".join([course.name for course in obj.courses_attending.all()])

    courses_attending_display.short_description = 'Courses Attending'

    list_display = (
        'full_name',
        'id_number',
        'date_of_entry',
        'signed_agreement',
        'courses_attending_display'
    )


class LecturerAdmin(admin.ModelAdmin):
    def courses_responsible_display(self, obj):
        return ", ".join([course.name for course in obj.courses_responsible.all()])

    courses_responsible_display.short_description = 'Courses Responsible'

    list_display = (
        'full_name',
        'courses_responsible_display'
    )


class UserMasterAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'location',
        'pedagogical_contact',
        'coaching_contact',
        'program_type'
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'platform',
        'category',
        'duration',
        'costs'
    )


class RoomResourceAdmin(admin.ModelAdmin):
    list_display = (
        'room_name',
        'seat',
        'module'
    )


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(UserMaster, UserMasterAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(RoomResource, RoomResourceAdmin)
