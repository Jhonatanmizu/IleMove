from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import AccountViews

urlpatterns = [
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("accounts/<uuid:pk>/", AccountViews.as_view(), name="account-detail"),
    path("accounts/", AccountViews.as_view(), name="account"),
]
