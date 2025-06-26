from django.urls import path

from .views import ExerciseCategoryViewSet, ExerciseViewSet

app_name = "exercise"

urlpatterns = [
    path("exercise", ExerciseViewSet.as_view(), name="exercise"),
    path(
        "exercise/<uuid:pk>/",
        ExerciseViewSet.as_view(),
        name="exercise-detail",
    ),
    path(
        "exercise_category",
        ExerciseCategoryViewSet.as_view(),
        name="exercise-category",
    ),
    path(
        "exercise_category/<uuid:pk>/",
        ExerciseCategoryViewSet.as_view(),
        name="exercise-category-detail",
    ),
]
