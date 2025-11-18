from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, PremiumUnlockViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'premium', PremiumUnlockViewSet, basename='premium')

urlpatterns = [
    path('', include(router.urls)),
]

