from django import forms
from .models import TicketBooking

class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = TicketBooking
        fields = ['name', 'email', 'concert', 'date', 'location', 'seats']
