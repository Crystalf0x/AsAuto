from django.shortcuts import render
from camping.models import Location
from camping.models import Spot
from camping.models import Accommodation
from camping.models import Room_type
from camping.models import Reviews
from camping.models import Booking
# Create your views here.


def location_view(request):
    location_list = Location.objects.all()

    context = {'location_view': location_list}
    return render(request, 'camping/location.html', context)


def spot_view(request):
    spot_list = Spot.objects.all()

    context = {'spot_view': spot_list}
    return render(request, 'camping/spot.html', context)


def accommodation_view(request):
    accommodation_list = Accommodation.objects.all()

    context = {'accommodation_view': accommodation_list}
    return render(request, 'camping/accommodation.html', context)


def room_type_view(request):
    room_type_list = Room_type.objects.all()

    context = {'room_type_view': room_type_list}
    return render(request, 'camping/room_type.html', context)


def reviews_view(request):
    reviews_list = Reviews.objects.all()

    context = {'reviews_view': reviews_list}
    return render(request, 'camping/reviews.html', context)


def booking_view(request):
    booking_list = Booking.objects.all()

    context = {'booking_view': booking_list}
    return render(request, 'camping/booking.html', context)



