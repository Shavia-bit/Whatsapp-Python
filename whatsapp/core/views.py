from .models import Order,ClientDetails,SalesInvoice,SalesOrder,DeliveryNote
from twilio.rest import Client
from notifications.settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render,redirect
from django.db.models import Q



# Create your views here.
# order_details = {
#     'amount': '5 Disk Brakes',
#     'item': 'Ducattis',
#     'date_of_delivery': '03/04/2024',
#     'address': 'No 1, WoodVale Street, Westlands, Nairobi'
# }

def home(request):
    return render(request,'home.html')

def search_clients(request):
    query = request.GET.get('search_query')
    
    if query:
        clients = ClientDetails.objects.filter(
            Q(client_name__icontains=query) |
            Q(whatsapp_number__icontains=query)
        )
    else:
        clients = ClientDetails.objects.all()

    context = {
        'clients': clients,
        'selected_client': None,
        'sales_orders': None,
        'search_query': query,
    }

    return render(request, 'sales_order_list.html', context)

def search_clients_delivery(request):
    query = request.GET.get('search_query')
    
    if query:
        clients = ClientDetails.objects.filter(
            Q(client_name__icontains=query) |
            Q(whatsapp_number__icontains=query)
        )
    else:
        clients = ClientDetails.objects.all()

    context = {
        'clients': clients,
        'selected_client': None,
        # 'sales_orders': None,
        'search_query': query,
    }

    return render(request, 'delivery_note.html', context)


def send_sales_order(request,client_id):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client_instance = get_object_or_404(ClientDetails, pk=client_id)
    user_whatsapp_number = client_instance.whatsapp_number
    orders = SalesOrder.objects.filter(client=client_instance) 
    print(f"Order: {orders}")
    for order in orders:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Your {} order of {} has shipped and should be delivered on {}. Details: {}'.format(
                order.total_order_value, order.order_number, order.delivery_address,
                order.delivery_address),
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )

        print(f"WhatsApp message sent to {user_whatsapp_number}, SID: {message.sid}")
        # return HttpResponse('Great! Expect a message...')
        return redirect('sales_order_list')
    else:
        return HttpResponse('No order details found in the database.')
    

def sales_order_list(request):
    # Retrieve the list of sales orders and their associated clients
    sales_orders = SalesOrder.objects.all()
    
    context = {
        'sales_orders': sales_orders,
    }
    
    return render(request, 'sales_order_list.html', context)

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
    sales_orders =None

    if query:
        clients = clients.filter(client_name__icontains=query)

    context = {
        'clients': clients,
        'selected_client': None, 
        'sales_orders': None 
    }


    selected_client_id = request.GET.get('client_id')
    print(f'selected_client_id: {selected_client_id}')

    if selected_client_id:
        selected_client = get_object_or_404(ClientDetails, pk=selected_client_id)
        sales_orders = SalesOrder.objects.filter(client=selected_client)
        context['selected_client'] = selected_client
        context['sales_orders'] = sales_orders


    return render(request,'sales_order.html',context)
def send_notification_view(request):
    client_id = request.GET.get('client_id')
    sales_order_id = request.GET.get('sales_order_id')


    
    # Retrieve the client and sales order objects using the IDs
    client = get_object_or_404(ClientDetails, pk=client_id)
    print(f'Number of Clients: {client.count()}')
    sales_order = get_object_or_404(SalesOrder, pk=sales_order_id)
    
    # Simulated notification sending logic (you can replace this with your actual logic)
    notification_sent = True
    
    if notification_sent:
        return render(request, 'send_sales.html', {'client': client, 'sales_order': sales_order})
    else:
        return HttpResponse("Failed to send notification.")

def delivery_note(request,client_id):

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client_instance = get_object_or_404(ClientDetails, pk=client_id)
    user_whatsapp_number = client_instance.whatsapp_number

    notes = DeliveryNote.objects.filter(client = client_instance)
    print(f"Delivery Notes: {notes}")

    for order in notes:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='The delivery for order date: {} for sales order: {} has shipped and should be delivered on {}. Details: {}'.format(
                order.delivery_date, order.sales_order, order.delivery_date,
                order),
            to='whatsapp:+{}'.format(user_whatsapp_number)
        )

        print(f"WhatsApp message sent to {user_whatsapp_number}, SID: {message.sid}")
        # return HttpResponse('Great! Expect a message...')
        return redirect('delivery_list')
    else:
        return HttpResponse('No order details found in the database.')


def deliveries_list(request):
    deliveries = DeliveryNote.objects.all()
    context = {
        'delivery_notes':deliveries,
    }

    return render(request,'delivery_note.html',context)


def sales_invoice(request):
    return render(request,'sales_invoice.html')


def clients(request):
    return render(request,'clients.html')
