import uuid

from django.db.models.manager import BaseManager
from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from app.utils.views.auth import AuthenticatedAPIView

from .models import CustomUser
from .serializers import CustomUserSerializer


class AccountViews(AuthenticatedAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self) -> BaseManager[CustomUser]:
        return CustomUser.objects.filter(is_active=True)

    def get(self, _: Request, pk: uuid.UUID) -> Response:
        user = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=200)

    def patch(self, request: Request, pk: uuid.UUID) -> Response:
        user = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, _: Request, pk: uuid.UUID) -> Response:
        user = get_object_or_404(self.get_queryset(), pk=pk)
        user.is_active = False
        user.save()
        return Response(status=204)
