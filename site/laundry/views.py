from django.shortcuts import render, redirect, HttpResponse
from . import forms, models
from django.urls import reverse
from .models import Reservation
# Create your views here.
def index(request):
   
    form = forms.ReserveForm()
    form1 = forms.ReserveForm(initial={'service_type': 'wash_fold'})
    form2 = forms.ReserveForm(initial={'service_type': 'express'})
    form3 = forms.ReserveForm(initial={'service_type': 'dry_clean'})
    rng_code = request.GET.get('code')

    if request.method == 'POST':
        form = forms.ReserveForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect(f"{reverse('laundry:index')}?code={reservation.rng_code}")
    

    return render(request, 'index.html', {
        'form': form,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'rng_code': rng_code
    })

from django.http import JsonResponse, Http404
from .models import Reservation

def get_completion_status(request):
    rng_code = request.GET.get('rng_code')
    if not rng_code:
        return JsonResponse({'error': 'rng_code parameter is required'}, status=400)

    try:
        reservation = Reservation.objects.get(rng_code=rng_code)
        return JsonResponse({'completion_status': reservation.completion_status})
    except Reservation.DoesNotExist:
        raise Http404("Reservation not found")
