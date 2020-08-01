from django.contrib import admin
from camping.models import Location
from camping.models import Spot
from camping.models import Accommodation
from camping.models import Room_type
from camping.models import Reviews
from camping.models import Booking

# Register your models here.
admin.site.register(Location)
admin.site.register(Spot)
admin.site.register(Accommodation)
admin.site.register(Room_type)
admin.site.register(Reviews)
admin.site.register(Booking)