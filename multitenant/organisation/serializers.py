from rest_framework.serializers import ModelSerializer

from .models import Employee, Projects


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

