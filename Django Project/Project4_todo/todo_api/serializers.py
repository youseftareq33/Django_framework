from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["task", "completed", "timestamp", "updated", "user"]





class TodoInputSerializer(serializers.Serializer):
    task = serializers.CharField(max_length=255)
    completed = serializers.BooleanField(default=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def validate_task(self, value):
        if not value.strip():
            raise serializers.ValidationError("Task cannot be empty.")
        return value

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance
    



class TodoOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'task', 'completed', 'timestamp', 'updated', 'user']