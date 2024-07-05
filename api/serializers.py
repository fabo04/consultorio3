from rest_framework import serializers
from .models import CustomUser, Role, Speciality, MedicalReport, Appointment

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['id', 'name']

class CustomUserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)
    speciality = SpecialitySerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'name', 'lastname', 'DNI', 'telephone', 'email', 'address', 'gender', 'birth_date', 'health_insurance', 'health_insurance_number', 'licence_number', 'speciality', 'notes', 'roles']

class MedicalReportSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(roles__name='professional'))
    patient = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(roles__name='patient'))

    class Meta:
        model = MedicalReport
        fields = ['id', 'professional', 'patient', 'date', 'hour', 'type', 'diagnosis', 'treatment', 'file']

class AppointmentSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(roles__name='professional'))
    patient = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.filter(roles__name='patient'))


    class Meta:
        model = Appointment
        fields = ['id', 'professional', 'patient', 'date', 'hour', 'status', 'notes']


class CustomUserCreateUpdateSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(many=True, queryset=Role.objects.all())
    speciality = serializers.PrimaryKeyRelatedField(queryset=Speciality.objects.all(), required=False, allow_null=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'name', 'lastname', 'DNI', 'telephone', 'email', 'address', 'gender', 'birth_date', 'health_insurance', 'health_insurance_number', 'licence_number', 'speciality', 'notes', 'roles']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        user.roles.set(roles_data)
        return user

    def update(self, instance, validated_data):
        roles_data = validated_data.pop('roles', None)
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        if roles_data is not None:
            instance.roles.set(roles_data)
        return instance


