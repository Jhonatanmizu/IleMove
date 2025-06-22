from django.db.models.manager import BaseManager
from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Workout
from .serializers import WorkoutSerializer


class WorkoutView(APIView):
    def get_queryset(self) -> BaseManager[Workout]:
        return Workout.objects.select_related("user").filter(is_active=True)

    def get(self, _: Request) -> Response:
        queryset = self.get_queryset()
        serializer = WorkoutSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self) -> HttpResponse:
        return HttpResponse("POST request received")

    def put(self) -> HttpResponse:
        return HttpResponse("PUT request received")

    def delete(self) -> HttpResponse:
        return HttpResponse("DELETE request received")

    def patch(self) -> HttpResponse:
        return HttpResponse("PATCH request received")
