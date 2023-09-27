from .models import Order,ClientDetails,SalesInvoice,SalesOrder,DeliveryNote
from twilio.rest import Client
from notifications.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
# order_details = {
#     'amount': '5 Disk Brakes',
#     'item': 'Ducattis',
#     'date_of_delivery': '03/04/2024',
#     'address': 'No 1, WoodVale Street, Westlands, Nairobi'
# }

def home(request):
    return render(request,'home.html')


def send_notification(request):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if request.method == 'POST':
        user_whatsapp_number = request.POST['user_number']

        #Retrieve Order details from database
        order = Order.objects.first()
        if order:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body='Your {} order of {} has shipped and should be delivered on {}. Details: {}'.format(
                    order.amount, order.item, order.date_of_delivery,
                    order.address),
                to='whatsapp:+{}'.format(user_whatsapp_number)
            )

            print(user_whatsapp_number)
            print(message.sid)
            return HttpResponse('Great! Expect a message...')
        else:
            return HttpResponse('No order details found in the database.')

    

    return render(request, 'phone.html')

def client_sales_order(request):
    query = request.GET.get('search_query')
    clients = ClientDetails.objects.all()

    if query:
        clients = clients.filter(client_name__icontains=query)

    context = {
        'clients': clients,
        'selected_client': None,
        'sales_orders': None,
    }

    selected_client_id = request.GET.get('client_id')
    print(f'selected_client_id: {selected_client_id}')

    if selected_client_id:
        selected_client = get_object_or_404(ClientDetails, pk=selected_client_id)
        sales_orders = SalesOrder.objects.filter(client=selected_client)
        context['selected_client'] = selected_client
        context['sales_orders'] = sales_orders

    return render(request,'sales_order.html',context)


def delivery_note(request):
    query = request.GET.get('search_query')
    clients = ClientDetails.objects.all()
    delivery_notes = DeliveryNote.objects.all()
    print(f'Number of DEliveries: {delivery_notes.count()}')
    print(f'Number of Clients: {clients.count()}')
    if query:
        clients = clients.filter(client_name__icontains=query)
        print(f'Filtered Clients: {clients.count()}')

    context = {
        'clients': clients,
        'selected_client': None,
        'delivery_notes': None,
    }

    selected_client_id = request.GET.get('client_id')
    print(f'selected_client_id: {selected_client_id}')
    
    if selected_client_id:
        selected_client = get_object_or_404(ClientDetails, pk=selected_client_id)
        delivery_notes = DeliveryNote.objects.filter(client=selected_client)
        print(f'Number of delivery notes: {delivery_notes.count()}')
        context['selected_client'] = selected_client
        context['delivery_notes'] = delivery_notes

    return render(request,'delivery_note.html',context)


def sales_invoice(request):
    return render(request,'sales_invoice.html')


def clients(request):
    return render(request,'clients.html')
