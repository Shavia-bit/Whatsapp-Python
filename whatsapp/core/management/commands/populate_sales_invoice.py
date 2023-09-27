from django.core.management.base import BaseCommand
from core.models import SalesInvoice, SalesOrder, DeliveryNote,ClientDetails  # Replace 'your_app_name' with your actual app name

class Command(BaseCommand):
    help = 'Populate the SalesInvoice table with dummy data'

    def handle(self, *args, **kwargs):

        client = ClientDetails.objects.create(
            
            client_name = 'Shaviya Kwoma',
            whatsapp_number= '792386418',
            email= 'client1@example.com',
            address= '123 Main Street, City'
            
        )
        
        # Add dummy sales invoice data
        dummy_sales_invoices = [
            {
                'invoice_date': '2023-01-25',
                'invoice_number': 'INV001',
                'sales_order_date': '2023-01-15',
                'sales_order': SalesOrder.objects.get(order_number='SO123'),
                'delivery_note_date': '2023-01-20',
                'delivery_note': DeliveryNote.objects.get(sales_order__order_number='SO123'),
                'total_invoice_value': 550.00,
                'tax_value': 50.00,
                'client':client
            },
            {
                'invoice_date': '2023-02-28',
                'invoice_number': 'INV002',
                'sales_order_date': '2023-02-20',
                'sales_order': SalesOrder.objects.get(order_number='SO456'),
                'delivery_note_date': '2023-02-25',
                'delivery_note': DeliveryNote.objects.get(sales_order__order_number='SO456'),
                'total_invoice_value': 880.00,
                'tax_value': 80.00,
                'client':client
            },
            # Add more dummy sales invoice data as needed
        ]

        for data in dummy_sales_invoices:
            sales_invoice = SalesInvoice(**data)
            sales_invoice.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the SalesInvoice table with dummy data.'))
