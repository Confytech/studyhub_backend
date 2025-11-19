from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, UserProfileView, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Router for the UserViewSet (CRUD)
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    # JWT login & refresh
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registration endpoint
    path('register/', RegisterView.as_view(), name='user-register'),

    # Profile endpoint
    path('profile/', UserProfileView.as_view(), name='user-profile'),

    # Include CRUD routes from router
    path('', include(router.urls)),
]

