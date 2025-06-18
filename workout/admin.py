from django.contrib import admin

from .models import Workout, WorkoutSession


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("name", "is_active")
    search_fields = ("name",)

@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("name", "is_active")
    search_fields = ("name",)
