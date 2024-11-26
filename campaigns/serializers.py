# campaigns/serializers.py
from rest_framework import serializers
from .models import Campaign

class CampaignSerializer(serializers.ModelSerializer):
    total_funded = serializers.DecimalField(read_only=True, max_digits=12, decimal_places=2)

    class Meta:
        model = Campaign
        fields = ['id', 'name', 'description', 'goal_amount', 'created_by', 'created_at', 'updated_at', 'total_funded']
