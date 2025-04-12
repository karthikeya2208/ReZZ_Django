from django.core.management.base import BaseCommand
from hotel.models import Hotel

class Command(BaseCommand):
    help = 'Populates the database with sample hotels'

    def handle(self, *args, **kwargs):
        hotels = [
            {"name": "Ocean View Hotel", "price": 120.00, "location": "Halifax", "availability": True},
            {"name": "Mountain Breeze Resort", "price": 95.50, "location": "Vancouver", "availability": True},
            {"name": "City Lights Inn", "price": 150.00, "location": "Toronto", "availability": False},
            {"name": "Lakeside Lodge", "price": 85.40, "location": "Montreal", "availability": True},
            {"name": "Sunset Retreat", "price": 110.00, "location": "Calgary", "availability": True},
            {"name": "Ocean View Hotel", "price": 120.75, "location": "Halifax", "availability": False},
            {"name": "Mountain Breeze Resort", "price": 95.50, "location": "Vancouver", "availability": True},
            {"name": "City Lights Inn", "price": 150.00, "location": "Toronto", "availability": False},
            {"name": "Lakeside Lodge", "price": 85.67, "location": "Montreal", "availability": True},
            {"name": "Sunset Retreat", "price": 110.00, "location": "Calgary", "availability": True},
            {"name": "The Barrington Hotel", "price": 137.00, "location": "Halifax", "availability": True},
            {"name": "Hotel Halifax", "price": 122.00, "location": "Halifax", "availability": True},
            {"name": "Atlantica Hotel Halifax", "price": 152.00, "location": "Halifax", "availability": True},
            {"name": "The Lord Nelson Hotel & Suites", "price": 177.00, "location": "Halifax", "availability": True},
            {"name": "Cambridge Suites Hotel", "price": 128.00, "location": "Halifax", "availability": False},
            {"name": "Prince George Hotel", "price": 180.30, "location": "Halifax", "availability": True},
            {"name": "The Sutton Place Hotel Halifax", "price": 242.00, "location": "Halifax", "availability": True},
            {"name": "Halifax Marriott Harbourfront Hotel", "price": 337.00, "location": "Halifax", "availability": True},
            {"name": "Future Inns Halifax", "price": 118.33, "location": "Halifax", "availability": True},
            {"name": "Coastal Inn Halifax", "price": 118.00, "location": "Halifax", "availability": True},
            {"name": "Granville Hall Residence", "price": 118.00, "location": "Halifax", "availability": True},
            {"name": "Best Western Plus Chocolate Lake Hotel", "price": 128.00, "location": "Halifax", "availability": True},
            {"name": "Chebucto Inn", "price": 170.18, "location": "Halifax", "availability": True},
            {"name": "Commons Inn", "price": 141.00, "location": "Halifax", "availability": False},
            {"name": "The Hollis Halifax a DoubleTree Suites by Hilton Hotel", "price": 173.00, "location": "Halifax", "availability": False},
            {"name": "Hampton Inn by Hilton Halifax Downtown", "price": 164.00, "location": "Halifax", "availability": True},
            {"name": "Chateau Bedford, Trademark Collection by Wyndham", "price": 160.00, "location": "Halifax", "availability": True},
            {"name": "The Westin Nova Scotian", "price": 152.00, "location": "Halifax", "availability": True},
            {"name": "Courtyard by Marriott Halifax Downtown", "price": 103.00, "location": "Halifax", "availability": True},
            {"name": "Moxy Halifax Downtown", "price": 196.00, "location": "Halifax", "availability": True},
            {"name": "Holiday Inn Express & Suites Halifax - Bedford", "price": 100.20, "location": "Halifax", "availability": True},
            {"name": "White Point Beach Resort", "price": 150.00, "location": "Hunts Point", "availability": True},
            {"name": "Holiday Inn Express & Suites Halifax Airport", "price": 128.00, "location": "Goffs", "availability": True},
            {"name": "Sandman Signature Dartmouth Hotel & Suites", "price": 139.00, "location": "Dartmouth", "availability": False},
            {"name": "Holiday Inn Express & Suites Halifax – Dartmouth", "price": 139.00, "location": "Dartmouth", "availability": True},
            {"name": "Hampton Inn & Suites by Hilton Halifax - Dartmouth", "price": 151.00, "location": "Dartmouth", "availability": True},
            {"name": "DoubleTree by Hilton Halifax Dartmouth", "price": 150.00, "location": "Dartmouth", "availability": True},
            {"name": "The Inn at Fisherman's Cove", "price": 160.00, "location": "Eastern Passage", "availability": True},
            {"name": "Brigantine Inn & Suites", "price": 110.90, "location": "Lunenburg", "availability": True},
            {"name": "Super 8 by Wyndham Windsor NS", "price": 90.00, "location": "Windsor", "availability": True},
            {"name": "Hearthstone Inn Boutique Hotel Halifax - Dartmouth", "price": 105.00, "location": "Dartmouth", "availability": True},
            {"name": "Residence Inn by Marriott Halifax Dartmouth", "price": 140.00, "location": "Dartmouth", "availability": True},
            {"name": "Courtyard by Marriott Halifax Dartmouth", "price": 130.45, "location": "Dartmouth", "availability": False},
            {"name": "Delta Hotels by Marriott Dartmouth", "price": 160.00, "location": "Dartmouth", "availability": True},
            {"name": "Lake City Motel", "price": 70.00, "location": "Dartmouth", "availability": False},
            {"name": "Comfort Inn Dartmouth", "price": 95.00, "location": "Dartmouth", "availability": True},
            {"name": "HFX Airport Hotel", "price": 115.00, "location": "Goffs", "availability": True},
            {"name": "Dalhousie University Accommodations", "price": 80.00, "location": "Halifax", "availability": True},
            {"name": "Mount Saint Vincent University Residence - Hostel", "price": 60.00, "location": "Halifax", "availability": True},
            {"name": "Stardust Motel Bedford", "price": 75.00, "location": "Bedford", "availability": True},
            {"name": "University of King's College", "price": 70.00, "location": "Halifax", "availability": True},
            {"name": "Saint Mary's University Residence Summer Accommodations", "price": 65.00, "location": "Halifax", "availability": True},
            {"name": "Highland Motel", "price": 78.00, "location": "Antigonish", "availability": True},
            {"name": "The Tidal Bore Inn", "price": 99.99, "location": "Maitland", "availability": True},
        ]

        for hotel_data in hotels:
            Hotel.objects.get_or_create(**hotel_data)

        self.stdout.write(self.style.SUCCESS('✅ Hotel data populated successfully.'))
