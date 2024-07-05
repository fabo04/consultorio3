from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import RoleViewSet, SpecialityViewSet, CustomUserViewSet, MedicalReportViewSet, AppointmentViewSet


router = DefaultRouter()
router.register(r'roles', RoleViewSet)
router.register(r'specialities', SpecialityViewSet)
router.register(r'users', CustomUserViewSet)
router.register(r'medical_reports', MedicalReportViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
