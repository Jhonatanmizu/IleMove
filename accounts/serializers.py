from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "birthdate",
            "identity_number",
            "phone_number",
            "address",
            "last_login",
            "date_joined",
            "is_active",
            "is_staff",
            "groups",
            "user_permissions",
        )
