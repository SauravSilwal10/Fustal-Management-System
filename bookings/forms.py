from django.forms import ModelForm
from bookings.models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['date']
        exclude = ('user',)
