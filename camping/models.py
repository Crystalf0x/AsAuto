from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings


class Location(models.Model):

    country = models.CharField(max_length=255, default='Romania')
    state = models.CharField(max_length=255, default='Dolj')
    city = models.CharField(max_length=255, default='Craiova')
    street = models.CharField(max_length=255, )
    street_no = models.DecimalField(max_digits=8, decimal_places=0)
    details = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.country


class Spot(models.Model):
    STATUS = (
            ('Available', 'Available'),
            ('Unavailable', 'Unavailable'),
            )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='Romania')
    image = models.ImageField(upload_to='property_picture/', blank=True, null=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, null=False, choices=STATUS)
    address = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    STATUS = (
            ('Available', 'Available'),
            ('Unavailable', 'Unavailable'),
            )

    HOUSE_TYPE = (
            ('Cottage', 'Cottage'),
            ('Cabin', 'Cabin'),
            ('Tent', 'Tent'),
            )

    BATHROOM_TYPE = (
            ('Communal', 'Communal'),
            ('Private', 'Private'),
            )
    name = models.CharField(max_length=255, default='Please insert the name of accommodation.')
    accommodation_type = models.CharField(max_length=200, null=False, choices=HOUSE_TYPE)
    bathroom_type = models.CharField(max_length=200, null=False, choices=BATHROOM_TYPE)
    status = models.CharField(max_length=200, null=False, choices=STATUS)
    spot = models.ForeignKey(Spot, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=150.99)
    icon_image = models.ImageField(upload_to='room_picture', blank=True, null=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    REVIEW = (
            ('*', '*'),
            ('**', '**'),
            ('***', '***'),
            ('****', '****'),
            ('*****', '*****'),)

    review = models.CharField(max_length=200, null=False, choices=REVIEW)
    comment = models.CharField(max_length=255)
    spot = models.OneToOneField(Spot, null=True, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.spot.name


class Room_type(models.Model):
    BED_TYPE = (
            ('Single', 'Single'),
            ('Double', 'Double'),
            ('Queen', 'Queen'),
            ('King', 'King'),
            )

    BATHROOM_TYPE = (
            ('Communal', 'Communal'),
            ('Private', 'Private'),
            )

    name = models.CharField(max_length=255, default='Accommodation')
    bed_count = models.DecimalField(max_digits=8, decimal_places=0)
    bed_type = models.CharField(max_length=200, null=False, choices=BED_TYPE)
    bathroom_type = models.CharField(max_length=200, null=False, choices=BATHROOM_TYPE)
    room_id = models.ForeignKey(Accommodation, null=True, on_delete=models.SET_NULL)
    icon_image = models.ImageField(upload_to='room_picture', blank=True, null=True)

    def __str__(self):
        return self.name


class Booking(models.Model):

    accommodation_id = models.ForeignKey(Accommodation, null=True, on_delete=models.SET_NULL)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adults = models.DecimalField(max_digits=8, decimal_places=0)
    children = models.DecimalField(max_digits=8, decimal_places=0)
    check_in_date = models.DateTimeField(default=timezone.now)
    check_out_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=15, decimal_places=0)

    def __str__(self):
        return self.name