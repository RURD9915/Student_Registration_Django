import csv
from django.core.management.base import BaseCommand
from enrollmentapp.models import Student

class Command(BaseCommand):
    help = 'Export students to CSV'

    def handle(self, *args, **kwargs):
        with open('students.csv', 'w', newline='') as csvfile:
            fieldnames = ['first_name', 'last_name', 'email', 'date_of_birth']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for student in Student.objects.all():
                writer.writerow({
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'email': student.email,
                    'date_of_birth': student.date_of_birth,
                })
        self.stdout.write(self.style.SUCCESS('Successfully exported students to CSV'))
