from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import Exercise


class ExerciseView(View):
    template_name = "exercise/pages/index.html"
    queryset = Exercise.objects.all()

    def get(self, request: HttpRequest) -> HttpResponse:
        exercise_id = request.GET.get("id")
        exercise = self.queryset.filter(id=exercise_id)
        context = {"exercise": exercise}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)

    def put(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)

    def delete(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
