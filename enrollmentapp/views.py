from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import StudentForm
from .models import Student
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import csv
import io

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Student registered successfully'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = StudentForm()
    
    return render(request, 'enrollment/register.html', {'form': form})

def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.drawString(100, height - 100, "Student List")

    y = height - 150
    for student in Student.objects.all():
        p.drawString(100, y, f"{student.first_name} {student.last_name} - {student.email}")
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    response.write(pdf)
    return response
