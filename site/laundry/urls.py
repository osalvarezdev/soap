from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'laundry'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-completion-status/', views.get_completion_status, name='get_completion_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)