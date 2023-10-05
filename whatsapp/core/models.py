from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Order(models.Model):
    amount = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    date_of_delivery = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.amount} order of {self.item}"
    

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.client_name
    
class ClientDetails(models.Model):
    client_name = models.CharField(max_length=255)
    whatsapp_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client_name


class SalesOrder(models.Model):
    client = models.ForeignKey(ClientDetails, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_number = models.CharField(max_length=100)
    order_details = models.TextField()
    delivery_address = models.TextField()
    total_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    tax_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_number

class MessageLog(models.Model):
    content = models.TextField()
    to_number = models.CharField(max_length=15)
    sid = models.CharField(max_length=64)
    status = models.CharField(max_length=20, default='pending')#Initial status set to pending
    
    def __str__(self):
        return f'SID: {self.sid}, Status: {self.status}'

class DeliveryNote(models.Model):
    client = models.ForeignKey(ClientDetails, on_delete=models.CASCADE)
    delivery_date = models.DateField()
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    sales_order_date = models.DateField()
    total_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Delivery Note {self.pk}"

class SalesInvoice(models.Model):
    client = models.ForeignKey(ClientDetails, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=100)
    sales_order_date = models.DateField()
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    delivery_note_date = models.DateField()
    delivery_note = models.ForeignKey(DeliveryNote, on_delete=models.CASCADE)
    total_invoice_value = models.DecimalField(max_digits=10, decimal_places=2)
    tax_value = models.DecimalField(max_digits=10, decimal_places=2)
    
    date_added = models.DateTimeField(default=timezone.now, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number



