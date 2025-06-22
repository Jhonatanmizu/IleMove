from typing import ClassVar

from rest_framework import serializers

from .models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model: ClassVar = Workout
        fields: ClassVar[list[str]] = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]
