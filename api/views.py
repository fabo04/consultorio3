from rest_framework import viewsets
from .models import CustomUser, Role, Speciality, MedicalReport, Appointment
from .serializers import CustomUserSerializer, CustomUserCreateUpdateSerializer, RoleSerializer, SpecialitySerializer, MedicalReportSerializer, AppointmentSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CustomUserCreateUpdateSerializer
        return CustomUserSerializer

class MedicalReportViewSet(viewsets.ModelViewSet):
    queryset = MedicalReport.objects.all()
    serializer_class = MedicalReportSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

