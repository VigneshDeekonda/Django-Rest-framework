from rest_framework import serializers
from students.models import Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"

        class StudentsSerializer(serializers.ModelSerializer):
            class Meta:
                model = Students
                fields = "__all__"