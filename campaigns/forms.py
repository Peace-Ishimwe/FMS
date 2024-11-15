# campaigns/forms.py
from django import forms
from .models import Campaign, Funding

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'description', 'goal_amount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-color focus:border-primary-color'}),
            'description': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-color focus:border-primary-color'}),
            'goal_amount': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-color focus:border-primary-color'}),
        }


class FundingForm(forms.ModelForm):
    class Meta:
        model = Funding
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary-color focus:border-primary-color'
            }),
        }
