from django.contrib import admin

from .models import Exercise, ExerciseCategory


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


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("name",)
