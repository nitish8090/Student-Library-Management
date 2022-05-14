from rest_framework import serializers

from .models import User, Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserSafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'role', 'date_joined']


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
