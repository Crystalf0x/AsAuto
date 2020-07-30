from django.urls import path
from camping.views import location_view
from camping.views import accommodation_view
# from camping.views import accommodation_type_view
from camping.views import spot_view
from camping.views import room_type_view
from camping.views import reviews_view
from camping.views import booking_view


app_name = 'properties'

urlpatterns = [path('', view=location_view, name='location'),
               path('accommodation/', view=accommodation_view, name='accommodation'),
               path('accommodation/room_type/', view=room_type_view, name='room_type'),
               path('spot/', view=spot_view, name='spot'),
               path('booking/', view=booking_view, name='booking'),
               path('reviews/', view=reviews_view, name='reviews'),
               ]