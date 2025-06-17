from django.contrib import admin

from .models import Exercise


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number_of_repetitions",
        "number_of_sets",
        "weight",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
