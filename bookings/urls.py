from django.urls import path
from . import views


urlpatterns = [
    path('bookings/', views.booking_view, name='booking'),
    path('mybookings/', views.mybookings, name='my-booking'),
    path('bookings/list/', views.manageBookings, name='list-booking'),
    path('esewa-request/', views.esewa_request, name='esewa-request'),
    path('bookings/esewa-verify/', views.esewa_verify, name='esewa-verify'),
]
