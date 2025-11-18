from django.db import models
from apps.users.models import User  # Assuming you have a custom User model

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    coins_added = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=[('pending','Pending'),('completed','Completed'),('failed','Failed')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.status}"

class PremiumUnlock(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="premium_status")
    is_premium = models.BooleanField(default=False)
    unlocked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Premium: {self.is_premium}"

