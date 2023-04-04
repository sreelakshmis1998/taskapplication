from rest_framework import serializers
from django.contrib.auth.models import User
from todo.models import Tasks

class UserSerializer(serializers.ModelSerializer):
    model=User
    fields=["username","email","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password","email"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class TaskSerizlizer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)

    class Meta:
        model=Tasks
        fields=["id","task_name","user","date","status"]