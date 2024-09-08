from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserCreateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("user_list/", UserListAPIView.as_view(), name="user-list"),
    # User registration
    path("register/", UserCreateAPIView.as_view(), name="register"),
    # JWT token
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token-refresh",
    ),
]