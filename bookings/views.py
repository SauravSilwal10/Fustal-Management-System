from django.shortcuts import render, redirect
from bookings.models import Arena, Timesheet, Booking, Date, PaymentMethod
from django.contrib.auth.decorators import login_required
from bookings.forms import BookingForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import requests
import xml.etree.ElementTree as ET
# Create your views here.

# Booking
@login_required(login_url="/login")
def booking_view(request):
    arena_list = Arena.objects.all()
    time_list = Timesheet.objects.all()
    date_list = Date.objects.all()
    booking_list = Booking.objects.all()
    new_list = Timesheet.objects.all()
    payment_list = PaymentMethod.objects.all()
    if request.method == 'POST' or None:
        Arenas = request.POST.get('Arenas')
        Times = request.POST.get('timings')
        Dates = request.POST.get('dates')
        PaymentMethods = request.POST.get('payment')
        conv_date = datetime.strptime(Dates, '%b %d, %Y').strftime('%Y-%m-%d')
        arena = Arena.objects.get(arenaname=Arenas)
        timesheet = Timesheet.objects.get(times=Times)
        date = Date.objects.get(dates=conv_date)
        payment_method = PaymentMethod.objects.get(payment_type=PaymentMethods)
        payment_mthd = str(payment_method)
        date.arena.add(arena)
        date.timesheet.add(timesheet)
        time_array = Timesheet.objects.all()
        date_array = date.timesheet.all()
        new_list = time_array.difference(date_array)
        create_booking = Booking(
            user=request.user, date=date, payment_method=payment_method)
        create_booking.save()
        if payment_mthd == "Esewa":
            return redirect(reverse("esewa-request") + "?b_id=" + str(create_booking.id))
        messages.info(request, 'Arena Booked Successfully.')
        print("sucessfully saved")
    new = new_list
    print(new)
    context = {"arena_list": arena_list,
               "time_list": time_list, "date_list": date_list, "news_list": new, "payment_type": payment_list}
    return render(request, "bookings.html", context)


# Manage Bookings
@login_required(login_url="/login")
def manageBookings(request):
    bookings = Booking.objects.all()
    context = {"booking_list": bookings}
    return render(request, "manage_bookings.html", context)

# My Bookings
@login_required(login_url="/login")
def mybookings(request):
    user = request.user
    context = {"user": user}
    return render(request, "mybookings.html", context)

# Integrating ESewa
def esewa_request(request):
    b_id = request.GET.get("b_id")
    booking = Booking.objects.get(id=b_id)
    context = {
        "booking": booking
    }
    return render(request, "esewa_request.html", context)

# ESewa verfication page
def esewa_verify(request):
    oid = request.GET.get("oid")
    amt = request.GET.get("amt")
    refId = request.GET.get("refId")
    print(oid, amt, refId)
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amt,
        'scd': 'EPAYTEST',
        'rid': 'refId',
        'pid': 'oid',
    }
    resp = requests.post(url, d)
    root = ET.fromstring(resp.content)
    status = (root[0].text.strip())
    booking_id = oid.split("_")[1]
    print(status)
    booking_obj = Booking.objects.get(id=booking_id)
    if status == "failure":
        booking_obj.payment_completed = True
        booking_obj.save()
        return redirect("/bookings")
    else:
        return redirect("/esewa-request/?b_id="+booking_id)


@csrf_exempt
def getAllDetails(request):
    if request.method == "GET":
        arena_list = Arena.objects.all()
        time_list = Timesheet.objects.all()
        bookings_list = Booking.objects.all()
        date_list = Date.objects.all()
        Dates = request.POST.get('dates')
        conv_date = datetime.strptime(
            Dates, '%b %d, %Y').strftime('%Y-%m-%d')
        date = Date.objects.get(dates=conv_date)
        time_array = Timesheet.objects.all()
        date_array = date.timesheet.all()
        new_list = time_array.difference(date_array)
        dateDictionary = {
            "arena_list": arena_list,
            "time_list": time_list, "bookings_list": bookings_list, "date_list": date_list,
            "new_list": new_list
        }
        return JsonResponse(dateDictionary)
    else:
        return JsonResponse({
            "message": "Only get request available"
        })
