from django.db import models
from authentication.models import CustomUser

class Campaign(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_campaigns')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_funded(self):
        return sum(funding.amount for funding in self.fundings.all())

    def __str__(self):
        return self.name

class Funding(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='fundings')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='fundings')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    funded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} funded {self.amount} to {self.campaign.name}"
