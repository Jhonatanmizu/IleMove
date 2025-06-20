from typing import ClassVar

from rest_framework import serializers

from .models import Exercise, ExerciseCategory


class ExerciseCategorySerializer(serializers.ModelSerializer):
    class Meta:
            model = ExerciseCategory
            fields: ClassVar = ["id", "name", "is_active", "created_at", "updated_at"]

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields:ClassVar = "__all__"
    exercise_category = ExerciseCategorySerializer(read_only=True)
