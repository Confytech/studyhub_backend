from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Transaction, PremiumUnlock
from .serializers import TransactionSerializer, PremiumUnlockSerializer
from rest_framework.permissions import IsAuthenticated

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Automatically associate the transaction with the logged-in user
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

class PremiumUnlockViewSet(viewsets.ModelViewSet):
    queryset = PremiumUnlock.objects.all()
    serializer_class = PremiumUnlockSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        return super().create(request, *args, **kwargs)

