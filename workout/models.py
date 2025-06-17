from django.contrib.auth.models import User
from django.db import models

from exercise.models import Exercise


class Workout(models.Model):
    class Meta:
        verbose_name = "Workout"
        verbose_name_plural = "Workouts"

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    exercises = models.ManyToManyField(Exercise)

    def __str__(self) -> str:
        return self.name
