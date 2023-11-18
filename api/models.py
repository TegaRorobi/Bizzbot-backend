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

