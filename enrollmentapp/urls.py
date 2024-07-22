from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register_student'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
     path('generate_csv/', views.generate_csv, name='generate_csv'), 
]