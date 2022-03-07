from django.shortcuts import render
from django.template.defaultfilters import date
from equipments.models import Equipment
from bookings.models import Booking, Date
from teams.models import Team
from tournaments.models import Tournament
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# Homepage
def home_view(request):
    return render(request, "home.html")

# Dashboard
@login_required(login_url="/login")
def dashboard_view(request):
    users = User.objects.count()
    bookings = Booking.objects.count()
    tournaments = Tournament.objects.count()
    teams = Team.objects.count()
    user_list = User.objects.all()
    context = {"user_count": users,
               "bookings_count": bookings, "tournaments_count": users, "teams_count": users, "user_list": user_list}
    return render(request, "dashboard.html", context)

# Add Date
@login_required(login_url="/login")
def addDate(request):
    if request.method == 'POST' or None:
        date = request.POST['d-date']
        create_date = Date(dates=date)
        create_date.save()
        messages.info(request, 'New date added successfully')
    return render(request, "date_timesheet.html")
