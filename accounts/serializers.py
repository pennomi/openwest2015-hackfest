from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password", "is_superuser", "is_staff", "groups", "user_permissions", )
        read_only_fields = ("is_active", "last_login", "date_joined",)