from django.core.management.base import BaseCommand
from core.models import ClientDetails  # Replace 'your_app_name' with your actual app name

class Command(BaseCommand):
    help = 'Populate the Client table with dummy data'

    def handle(self, *args, **kwargs):
        # Add dummy client data
        dummy_clients = [
            {
                'client_name': 'Client 1',
                'whatsapp_number': '792386418',
                'email': 'client1@example.com',
                'address': '123 Main Street, City'
            },
            {
                'client_name': 'Client 2',
                'whatsapp_number': '9876543210',
                'email': 'client2@example.com',
                'address': '456 Elm Street, Town'
            },
            # Add more dummy client data as needed
        ]

        for data in dummy_clients:
            client = ClientDetails(**data)
            client.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the Client table with dummy data.'))
