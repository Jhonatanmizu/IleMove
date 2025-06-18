from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class WorkoutView(View):
    template_name = "workout/workout.html"
    def __init__(self) -> None:
        self.name = "WorkoutView"

    def get(self) -> HttpResponse:
        return render(self.request, self.template_name)

    def post(self) -> HttpResponse:
        return HttpResponse("POST request received")

    def put(self) -> HttpResponse:
        return HttpResponse("PUT request received")

    def delete(self) -> HttpResponse:
        return HttpResponse("DELETE request received")

    def patch(self) -> HttpResponse:
        return HttpResponse("PATCH request received")
