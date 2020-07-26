import datetime
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

class Accommodation(models.Model):
    def clean(self):
        if self.status == 'tent' and self.pub_date is not None:
            raise ValidationError(_('You cannot have a private bathroom at a tent.'))

