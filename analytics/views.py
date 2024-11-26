from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from campaigns.models import Funding, Campaign
from django.db.models import Sum, F

@login_required
def funding_analytics(request):
    user = request.user
    # Data Preparation
    funding_data = Funding.objects.filter(user=user).select_related('campaign')
    # Total funded per campaign
    campaigns_funded = funding_data.values('campaign__name').annotate(
        total_funded=Sum('amount')
    ).order_by('-total_funded')

    # Monthly funding activity
    monthly_funding = funding_data.annotate(
        month=F('funded_at__month'),
        year=F('funded_at__year')
    ).values('month', 'year').annotate(
        total=Sum('amount')
    ).order_by('year', 'month')

    # Total funding and goal comparison
    campaigns = Campaign.objects.filter(fundings__user=user).distinct()
    funding_vs_goal = [
        {
            'campaign': campaign.name,
            'goal': campaign.goal_amount,
            'funded': campaign.total_funded()
        }
        for campaign in campaigns
    ]

    # Convert Decimal to float or integer
    campaigns_funded_data = [
        {
            'campaign__name': item['campaign__name'],
            'total_funded': float(item['total_funded']) if item['total_funded'] else 0
        }
        for item in campaigns_funded
    ]

    monthly_funding_data = [
        {
            'month': item['month'],
            'year': item['year'],
            'total': float(item['total']) if item['total'] else 0
        }
        for item in monthly_funding
    ]

    funding_vs_goal_data = [
        {
            'campaign': item['campaign'],
            'goal': float(item['goal']) if item['goal'] else 0,
            'funded': float(item['funded']) if item['funded'] else 0
        }
        for item in funding_vs_goal
    ]

    # Return data as JSON
    context = {
        'campaigns_funded': campaigns_funded_data,
        'monthly_funding': monthly_funding_data,
        'funding_vs_goal': funding_vs_goal_data
    }
    return render(request, 'funding_analytics.html', context)