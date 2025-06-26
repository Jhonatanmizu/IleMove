import uuid

from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from app.utils.views.auth import AuthenticatedAPIView

from .models import Workout
from .serializers import WorkoutSerializer


class WorkoutView(AuthenticatedAPIView):
    serializer_class = WorkoutSerializer

    def get_queryset(self) -> BaseManager[Workout]:
        return Workout.objects.select_related("user").filter(is_active=True)

    def get(self, _: Request, pk: uuid.UUID | None = None) -> Response:
        if pk:
            workout = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = WorkoutSerializer(workout)
            return Response(serializer.data, status=status.HTTP_200_OK)
        workout = self.get_queryset()
        serializer = WorkoutSerializer(workout, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request: Request, pk: uuid.UUID) -> HttpResponse:
        workout = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(workout, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, _: Request, pk: uuid.UUID) -> Response:
        workout = get_object_or_404(self.get_queryset(), pk=pk)
        workout.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
