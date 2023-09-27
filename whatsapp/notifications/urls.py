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

from core.views import send_notification,home,client_sales_order,delivery_note



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('send_notification/',send_notification,name='send_notification'),
    path('client_sales_orders/',client_sales_order,name = 'cliet_sales_order'),
    path('delivery_note/',delivery_note,name='delivery_notes')
    # path('',send_notification)
]
