from django import forms
from . import models

class ReserveForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = [
            'name', 'phone_number', 'service_type',
            'pickup_required', 'pickup_address', 'pickup_time',
            'delivery_required', 'delivery_address', 'delivery_time'
        ]
        widgets = {
                    'name': forms.TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter your full name'
                    }),
                    'phone_number': forms.TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Enter your phone number'
                    }),
                    'pickup_address': forms.Textarea(attrs={
                        'class': 'form-control',
                        'rows': 3,
                        'placeholder': 'Enter pickup address'
                    }),
                    'delivery_address': forms.Textarea(attrs={
                        'class': 'form-control',
                        'rows': 3,
                        'placeholder': 'Enter delivery address'
                    }),
                    'pickup_time': forms.DateTimeInput(attrs={
                        'class': 'form-control',
                        'type': 'datetime-local'
                    }),
                    'delivery_time': forms.DateTimeInput(attrs={
                        'class': 'form-control',
                        'type': 'datetime-local'
                    }),
                    'service_type': forms.Select(attrs={
                        'class': 'form-control'
                    }),
                    'pickup_required': forms.CheckboxInput(attrs={
                        'class': 'form-check-input'
                    }),
                    'delivery_required': forms.CheckboxInput(attrs={
                        'class': 'form-check-input'
                    }),
                }