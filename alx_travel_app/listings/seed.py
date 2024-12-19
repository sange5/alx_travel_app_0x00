from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        listings = [
            {"title": "Cozy Apartment", "description": "A cozy apartment in the city center.", "price_per_night": 100, "location": "New York"},
            {"title": "Beachfront Villa", "description": "A luxurious villa by the beach.", "price_per_night": 250, "location": "Miami"},
            {"title": "Mountain Cabin", "description": "A peaceful cabin in the mountains.", "price_per_night": 150, "location": "Denver"},
        ]
        for listing in listings:
            Listing.objects.create(**listing)
        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
