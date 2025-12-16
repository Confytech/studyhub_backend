from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.payments.models import Transaction, PremiumUnlock, CoinReward
from apps.users.models import User

# ----------------------------------
# Handle completed transactions
# ----------------------------------
@receiver(post_save, sender=Transaction)
def handle_transaction(sender, instance, created, **kwargs):
    if instance.status == 'completed':
        # Add coins to user's balance
        user = instance.user
        user.coins += instance.coins_added
        user.save()

        # Unlock premium if coins_added crosses a threshold (example)
        if instance.coins_added >= 100:  # Example condition
            premium, _ = PremiumUnlock.objects.get_or_create(user=user)
            premium.is_premium = True
            premium.unlocked_at = instance.updated_at
            premium.save()

# ----------------------------------
# Optional: Track coin rewards
# ----------------------------------
@receiver(post_save, sender=CoinReward)
def award_coins(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.coins += instance.coins
        user.save()

