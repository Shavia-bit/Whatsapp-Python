from django.core.management.base import BaseCommand
from core.models import DeliveryNote, SalesOrder,ClientDetails  # Replace 'your_app_name' with your actual app name

class Command(BaseCommand):
    help = 'Populate the DeliveryNote table with dummy data'

    def handle(self, *args, **kwargs):
        client = ClientDetails.objects.create(
            
                client_name = 'Shaviya Kwoma',
                whatsapp_number= '792386418',
                email= 'client1@example.com',
                address= '123 Main Street, City'
            
        )
        # Add dummy delivery note data
        dummy_delivery_notes = [
            {
                'delivery_date': '2023-01-20',
                'sales_order': SalesOrder.objects.get(order_number='SO123'),
                'sales_order_date': '2023-01-15',
                'total_order_value': 500.00,
                'client':client
            },
            {
                'delivery_date': '2023-02-25',
                'sales_order': SalesOrder.objects.get(order_number='SO456'),
                'sales_order_date': '2023-02-20',
                'total_order_value': 800.00,
                'client':client
            },
            # Add more dummy delivery note data as needed
        ]

        for data in dummy_delivery_notes:
            delivery_note = DeliveryNote(**data)
            delivery_note.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the DeliveryNote table with dummy data.'))
