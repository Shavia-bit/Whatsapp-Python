from typing import Any
from django.core.management.base import BaseCommand

from core.models import Order


class Command(BaseCommand):
    help="Populate the database with dummy order details"

    def handle(self, *args, **kwargs):
        Order.objects.create(
            amount = '10',
            item = 'Ducatti Brake Disks',
            date_of_delivery = '2024-10-16',
            address = 'No 1, WoodVale Street, Westlands, Nairobi'
        )
        self.stdout.write(self.style.SUCCESS('Database Successfully populated!'))