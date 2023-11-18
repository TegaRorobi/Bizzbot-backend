
from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext as _


class OpeningDay(BaseModel):

    DAY_CHOICES = [
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    day = models.CharField(_('Day of the Week'), choices=DAY_CHOICES, max_length=20)
    opening_time = models.TimeField(_('Opening Time'))
    closing_time = models.TimeField(_('Closing Time'))

    def __str__(self):
        return f'{self.day}, {self.opening_time.strftime("%I:%M %p")} to {self.closing_time.strftime("%I:%M %p")}'