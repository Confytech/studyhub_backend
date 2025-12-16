# apps/users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, UserProfileView, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Router for UserViewSet (CRUD operations)
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # JWT login & refresh endpoints
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User registration endpoint
    path('register/', RegisterView.as_view(), name='user-register'),

    # User profile endpoint (authenticated)
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    # Include the router-generated CRUD endpoints
    path('', include(router.urls)),
]

