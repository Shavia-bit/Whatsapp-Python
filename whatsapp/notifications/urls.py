"""notifications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import CustomLoginView, register, send_invoice,clients, sales_invoice,sales_order_list, search_clients, send_notification,home,client_sales_order,delivery_note, send_notification_view, send_sales_order,deliveries_list,search_clients_delivery,dashboard,message_logs, token_verification



urlpatterns = [
    path('accounts/login/',CustomLoginView.as_view(),name='login'),
    path('admin/', admin.site.urls),
    path('register/',register, name='register'),
    path('token-verification/', token_verification, name='token_verification'),
    path('',home,name='home'),
    path('send_notification/',send_notification,name='send_notification'),
    path('client_sales_orders/',client_sales_order,name = 'cliet_sales_order'),
    path('delivery_note/<int:client_id>/',delivery_note,name='delivery_notes'),
    path('send_invoice/<int:client_id>/',send_invoice,name='send_invoice'),
    path('send_notification_view/', send_notification_view, name='send_notification_view'),
    path('sales_order_list/', sales_order_list, name='sales_order_list'),
    path('delivery_list/',deliveries_list,name='delivery_list'),
    path('send_whatsapp_message/<int:client_id>/', send_sales_order, name='send_whatsapp_message'),
    path('search/', search_clients, name='search_clients'),
    path('search_deliveries/',search_clients_delivery,name='search_client_deliveries'),
    path('dashboard/', dashboard, name='dashboard'),
    path('clients/', clients, name='client_list'),
    path('message_logs/', message_logs, name='message_logs'),
    path('sales_invoices/',sales_invoice, name='sales_invoices')
]
