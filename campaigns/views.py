# campaigns/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import CampaignForm, FundingForm
from .models import Campaign
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Campaign
from .serializers import CampaignSerializer

# List all campaigns
def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign_list.html', {'campaigns': campaigns})

class CampaignListView(APIView):
    def get(self, request):
        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create new campaign - only for Admin role
@login_required
def campaign_create(request):
    if request.user.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to create a campaign.")
    
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.created_by = request.user
            campaign.save()
            return redirect('campaigns:campaign_list')
    else:
        form = CampaignForm()
    return render(request, 'campaign_form.html', {'form': form})


@login_required
def campaign_detail(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    form = FundingForm()
    if request.method == 'POST':
        form = FundingForm(request.POST)
        if form.is_valid():
            funding = form.save(commit=False)
            funding.campaign = campaign
            funding.user = request.user
            funding.save()
            return redirect('campaigns:campaign_detail', campaign_id=campaign.id)

    context = {
        'campaign': campaign,
        'form': form,
        'total_funded': campaign.total_funded(),
    }
    return render(request, 'campaign_detail.html', context)

@login_required
def campaign_update(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)

    # Check if the user is the creator of the campaign or an admin
    if request.user != campaign.created_by and request.user.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to update this campaign.")

    if request.method == 'POST':
        form = CampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            messages.success(request, "Campaign updated successfully.")
            return redirect('campaigns:campaign_detail', campaign_id=campaign.id)
    else:
        form = CampaignForm(instance=campaign)

    context = {
        'form': form,
        'campaign': campaign
    }
    return render(request, 'campaign_update_form.html', context)