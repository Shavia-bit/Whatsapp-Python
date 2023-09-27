from django.contrib import admin

from core.models import ClientDetails, DeliveryNote, SalesInvoice, SalesOrder

# Register your models here.
admin.site.register(SalesInvoice)
admin.site.register(SalesOrder)
admin.site.register(DeliveryNote)
admin.site.register(ClientDetails)
