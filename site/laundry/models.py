from django.db import models
import random, string
from django.utils import timezone

# Create your models here.

def generate_rng_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


class Reservation(models.Model):

    # Customer Information
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    rng_code = models.CharField(max_length=10, unique=True, default=generate_rng_code)

     # Service Details
    SERVICE_CHOICES = [
        ('wash_fold', 'Wash & Fold'),
        ('express', 'Express Service'),
        ('dry_clean', 'Dry Cleaning'),
    ]
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Pickup and Delivery Options
    pickup_required = models.BooleanField(default=False)
    pickup_address = models.TextField(blank=True, null=True)
    pickup_time = models.DateTimeField(blank=True, null=True)

    delivery_required = models.BooleanField(default=False)
    delivery_address = models.TextField(blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)

    # Tracking
    reservation_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    payment_status = models.CharField(max_length=20, choices=[('unpaid', 'Unpaid'), ('paid', 'Paid')], default='unpaid')
    completion_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    completion_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        
        if not self.rng_code:
            while True:
                self.rng_code = generate_rng_code()
                if not Reservation.objects.filter(rng_code=self.rng_code).exists():
                    break

        if not self.pickup_required:
            self.pickup_address = None
            self.pickup_time = None

        if not self.delivery_required:
            self.delivery_address = None
            self.delivery_time = None

        if self.weight_kg is not None:
            self.price = self.weight_kg * 35
        else:
            self.price = None  

        if self.completion_status == 'completed' and self.completion_date is None:
            self.completion_date = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.service_type}"