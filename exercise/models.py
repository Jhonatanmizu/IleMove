from django.contrib.auth import get_user_model
from django.db import models


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
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="exercises",
    )

    def __str__(self) -> str:
        return self.name
