

from django.urls import path

from .views import ExerciseCategoryViewSet, ExerciseViewSet

app_name = "exercise"

urlpatterns = [
    path("api/v1/exercise", ExerciseViewSet.as_view(), name="exercise"),
    path("api/v1/exercise/<int:pk>/", ExerciseViewSet.as_view(),
        name="exercise-detail"),
    path("api/v1/exercise_category", ExerciseCategoryViewSet.as_view(),
        name="exercise-category"),
    path("api/v1/exercise_category/<int:pk>/", ExerciseCategoryViewSet.as_view(),
        name="exercise-category-detail")
]
