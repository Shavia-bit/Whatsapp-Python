from django.core.management.base import BaseCommand
from core.models import SalesOrder,ClientDetails     # Replace 'your_app_name' with your actual app name

class Command(BaseCommand):
    help = 'Populate the SalesOrder table with dummy data'

    def handle(self, *args, **kwargs):
        client = ClientDetails.objects.create(
            
                client_name = 'Shaviya Kwoma',
                whatsapp_number= '792386418',
                email= 'client1@example.com',
                address= '123 Main Street, City'
            
        )
        # Add dummy sales order data
        dummy_sales_orders = [
            {
                'order_date': '2023-01-15',
                'order_number': 'SO123',
                'order_details': 'Sample order details for SO123',
                'delivery_address': '123 Main Street, City',
                'total_order_value': 500.00,
                'tax_value': 50.00,
                'client':client
            },
            {
                'order_date': '2023-02-20',
                'order_number': 'SO456',
                'order_details': 'Sample order details for SO456',
                'delivery_address': '456 Elm Street, Town',
                'total_order_value': 800.00,
                'tax_value': 80.00,
                'client':client
            },
            # Add more dummy sales order data as needed
        ]

        for data in dummy_sales_orders:
            sales_order = SalesOrder(**data)
            sales_order.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the SalesOrder table with dummy data.'))
