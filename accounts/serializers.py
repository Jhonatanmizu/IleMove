from rest_framework import serializers

from .models import Address, CustomUser, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "user",
            "bio",
            "birthdate",
            "identity_number",
            "phone_number",
            "photo",
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "street",
            "city",
            "state",
            "country",
            "zip_code",
            "user",
        )


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "last_login",
            "date_joined",
            "is_active",
            "is_staff",
            "groups",
            "user_permissions",
        )

    address = AddressSerializer(many=True, read_only=True)
    profile = ProfileSerializer(read_only=True)
