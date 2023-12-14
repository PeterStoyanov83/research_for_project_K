from django.core.management.base import BaseCommand
from django.utils import timezone
from django_peter1.accounts.models import UserMaster, Course, Participant, RoomResource, Lecturer


class Command(BaseCommand):
    help = 'Populates the database with initial test data'

    def handle(self, *args, **kwargs):
        # Create Courses
        course1 = Course.objects.create(
            name="Intro to Programming",
            description="An introductory course on programming",
            platform="Online",
            category="IT",
            duration=timezone.timedelta(days=30),
            costs=500
        )
        course2 = Course.objects.create(
            name="Advanced Pottery",
            description="A comprehensive look at advanced pottery techniques",
            platform="In-person",
            category="Arts",
            duration=timezone.timedelta(days=60),
            costs=300
        )

        # Create Participants
        participant1 = Participant.objects.create(
            full_name="Alice Johnson",
            id_number="P10001",
            date_of_entry=timezone.now(),
            signed_agreement=True,
            period_of_stay='6 months'
        )
        participant1.courses_attending.add(course1)

        # Create UserMaster
        user_master1 = UserMaster.objects.create(
            first_name="John",
            last_name="Doe",
            location="Office Center",
            pedagogical_contact="Jane Smith",
            coaching_contact="Max Power",
            program_type="Rehabilitation"
        )

        # Create RoomResource
        room_resource1 = RoomResource.objects.create(
            room_name="Room A",
            seat=25,
            module="Morning Module"
        )

        # Create Lecturer
        lecturer1 = Lecturer.objects.create(
            full_name="Dr. Sarah Connors",
            bio="PhD in Computer Science with a focus on AI and ML."
        )
        lecturer1.courses_responsible.add(course1)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
