from django.contrib import admin
from .models import Arena
from .models import Timesheet
from .models import Booking
from .models import Date
from .models import PaymentMethod

# Register your models here.
admin.site.register(Arena)
admin.site.register(Timesheet)
admin.site.register(Booking)
admin.site.register(Date)
admin.site.register(PaymentMethod)
