from rest_framework import serializers
from .models import Task, CustomUser
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']




class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = '__all__'
        
        
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {
            "validators": UniqueValidator(CustomUser.objects.all(), 'An account already exists'),
            "password":{
                "write_only": True,
                "allow_blank": False
            }
        }
        
        

        