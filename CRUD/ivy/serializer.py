from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

        def validate_roll(self,value):
            if value>=200:
                raise serializers.ValidationError('seat full')
            return value