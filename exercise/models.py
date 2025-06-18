from django.contrib.auth.models import User
from django.db import models


class ExerciseCategory(models.Model):
    class Meta:
        verbose_name = "Exercise Category"
        verbose_name_plural = "Exercise Categories"

    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="exercise_categories",
    )

    def __str__(self) -> str:
        return self.name


class Exercise(models.Model):
    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    number_of_repetitions = models.IntegerField()
    number_of_sets = models.IntegerField()
    weight = models.IntegerField()
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="exercises",
    )
    exercise_category = models.ForeignKey(
        ExerciseCategory,
        on_delete=models.SET_NULL,
        related_name="exercises",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name
