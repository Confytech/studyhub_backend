from django.db import models
from apps.users.models import User  # Custom User model

# ----------------------------------
# TRANSACTIONS
# ----------------------------------
class Transaction(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    coins_added = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Track status changes

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.status}"

# ----------------------------------
# PREMIUM STATUS
# ----------------------------------
class PremiumUnlock(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="premium_status"
    )
    is_premium = models.BooleanField(default=False)
    unlocked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        status = "Premium" if self.is_premium else "Free"
        return f"{self.user.username} - {status}"

# ----------------------------------
# OPTIONAL: COIN REWARDS / BADGES (future expansion)
# ----------------------------------
class CoinReward(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="coin_rewards"
    )
    description = models.CharField(max_length=255)
    coins = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - +{self.coins} coins - {self.description}"

