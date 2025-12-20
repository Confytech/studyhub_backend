# apps/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserProfileView, UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')  # ✅ no duplicate "users"

urlpatterns = [
    # JWT auth
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Register
    path('register/', RegisterView.as_view(), name='user-register'),

    # ✅ THIS IS THE IMPORTANT FIX
    path('me/', UserProfileView.as_view(), name='user-me'),

    # CRUD
    path('', include(router.urls)),
]

