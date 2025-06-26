import uuid

from django.db.models.manager import BaseManager
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from app.utils.views.auth import AuthenticatedAPIView

from .models import Exercise, ExerciseCategory
from .serializers import ExerciseCategorySerializer, ExerciseSerializer


class ExerciseViewSet(AuthenticatedAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self) -> BaseManager[Exercise]:
        queryset = Exercise.objects.filter(is_active=True)
        return queryset.select_related("exercise_category", "user")

    def get(self, _: Request, pk: uuid.UUID | None = None) -> Response:
        if pk:
            exercise = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.serializer_class(exercise)
        else:
            exercises = self.get_queryset()
            serializer = self.serializer_class(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, pk: uuid.UUID) -> Response:
        exercise = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _: Request, pk: uuid.UUID) -> Response:
        exercise = get_object_or_404(self.get_queryset(), pk=pk)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExerciseCategoryViewSet(APIView):
    serializer_class = ExerciseCategorySerializer

    def get_queryset(self) -> BaseManager[ExerciseCategory]:
        queryset = ExerciseCategory.objects.filter(is_active=True)
        return queryset.select_related("user")

    def get(self, _: Request, pk: uuid.UUID | None = None) -> Response:
        if pk:
            exercise_category = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.serializer_class(exercise_category)
        else:
            exercise_categories = self.get_queryset()
            serializer = self.serializer_class(exercise_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, pk: uuid.UUID) -> Response:
        exercise_category = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(exercise_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _: Request, pk: uuid.UUID) -> Response:
        exercise_category = get_object_or_404(self.get_queryset(), pk=pk)
        exercise_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
