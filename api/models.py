from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext as _
from datetime import timedelta

from django.contrib.auth import get_user_model
UserModel = get_user_model()


class Product(BaseModel):

    seller = models.ForeignKey(UserModel, verbose_name=('Product Owner'), on_delete=models.CASCADE)
    name = models.CharField(_('Product Name'), max_length=255)
    price = models.DecimalField(_('Product Price'), max_digits=15, decimal_places=2, default=0.00)
    inventory = models.IntegerField(_('Product Inventory'), default=0)
    delivery_time = models.DurationField(default=timedelta(hours=1, minutes=30))

    def __str__(self) -> str:
        return f"{self.name} [{self.price}]"


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

    day = models.CharField(_('Day of the Week'), max_length=20)
    opening_time = models.TimeField(_('Opening Time'))
    closing_time = models.TimeField(_('Closing Time'))

    def __str__(self):
        return f'{self.day}, {self.opening_time.strftime("%I:%M %p")} to {self.closing_time.strftime("%I:%M %p")}'

