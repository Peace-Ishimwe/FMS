from django.core.management.base import BaseCommand
from authentication.models import CustomUser
from campaigns.models import Campaign, Funding
from faker import Faker
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Populate database with fake users, campaigns, and funding data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create sample users if not already existing
        users = []
        for _ in range(50):  # Create 50 fake users
            user = CustomUser.objects.create_user(
                email=fake.email(),
                password="password1234",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                province=random.choice(['kigali', 'northern', 'southern', 'eastern', 'western']),
                sector=random.choice(['Agriculture', 'Trading']),
                role=random.choice(['Admin', 'User']),
            )
            users.append(user)

        # Generate 100 campaigns
        campaigns = []
        for _ in range(100):  # Create 100 campaigns
            campaign = Campaign.objects.create(
                name=fake.company(),
                description=fake.text(),
                goal_amount=Decimal(random.randint(1000, 10000)),
                created_by=random.choice(users),
            )
            campaigns.append(campaign)

        # Generate 500 funding records
        for _ in range(500):  # Create 500 funding records
            user = random.choice(users)
            campaign = random.choice(campaigns)
            Funding.objects.create(
                user=user,
                campaign=campaign,
                amount=Decimal(random.randint(10, 500)),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake data'))