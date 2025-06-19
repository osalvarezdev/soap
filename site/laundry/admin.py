from django.contrib import admin
from django.contrib.admin import AdminSite
from . import models

# Register your models here.
class MyAdminSite(AdminSite):
    site_header = "Laundry Admin"
    site_title = "Laundry Management System"
    index_title = "Dashboard"

# Replace the default admin instance
custom_admin_site = MyAdminSite(name='custom_admin')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'rng_code', 'service_type', 'weight_kg', 'price', 
                    'pickup_required', 'pickup_address', 'pickup_time', 
                    'delivery_required', 'delivery_address', 'delivery_time',
                    'reservation_date', 'payment_status', 'completion_status', 'completion_date')
    search_fields = ('name', 'phone_number', 'rng_code')
    readonly_fields = ('rng_code', 'reservation_date', 'completion_date')
    list_filter = ('service_type', 'payment_status', 'completion_status')

custom_admin_site.register(models.Reservation, ReservationAdmin)