from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrative'),
        ('professional', 'Professional'),
        ('patient', 'Patient'),
    ]

    name = models.CharField(max_length=15, choices=ROLE_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Speciality(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    roles = models.ManyToManyField(Role, related_name='users')
    DNI = models.CharField(max_length=10, unique=True)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    health_insurance = models.CharField(max_length=100, blank=True, null=True)
    health_insurance_number = models.CharField(max_length=20, blank=True, null=True)
    licence_number = models.CharField(max_length=20, blank=True, null=True)
    speciality = models.ForeignKey('Speciality', on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f'{self.username} ({self.get_full_name()})'


class MedicalReport(models.Model):
    professional = models.ForeignKey(CustomUser, related_name='professional_reports', on_delete=models.CASCADE)
    patient = models.ForeignKey(CustomUser, related_name='patient_reports', on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    type = models.CharField(max_length=50)
    diagnosis = models.TextField()
    treatment = models.TextField()
    file = models.FileField(upload_to='medical_reports/', blank=True, null=True)

    def __str__(self):
        return f'Report {self.id} by {self.professional}'

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    professional = models.ForeignKey(CustomUser, related_name='professional_appointments', on_delete=models.CASCADE)
    patient = models.ForeignKey(CustomUser, related_name='patient_appointments', on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Appointment {self.id} on {self.date} at {self.hour}'

