# myapp/views/base.py

from typing import ClassVar

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class AuthenticatedAPIView(APIView):
    authentication_classes: ClassVar = [JWTAuthentication]
    permission_classes: ClassVar = [IsAuthenticated]
