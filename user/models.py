from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext as _

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from .manager import UserManager



class User(AbstractUser):

    BUSINESS_CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Lifestyle', 'Lifestyle'),
        ('Health', 'Health'),
        ('Food', 'Food'),
        ('Banking', 'Banking'),
        ('Aviation', 'Aviation'),
        ('E-commerce', 'E-commerce'),
        ('Vehicles & Automobiles', 'Vehicles & Automobiles'),
        ('Agriculture', 'Agriculture'),
    ]

    full_name = models.CharField(_('Full Name'), max_length=200, null=True, blank=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        help_text=_("Not Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[UnicodeUsernameValidator()],
        error_messages={"unique": _("A user with that username already exists."),},
        null=True, 
        blank=True
    )
    email = models.EmailField(_('Email Address'), unique=True)
    country = CountryField(null=True)
    phone_number = PhoneNumberField(null=True)

    business_category = models.CharField(_('Business Category'), choices=BUSINESS_CATEGORY_CHOICES, max_length=30, null=True)
    business_name = models.CharField(_('Business Name'), max_length=200, null=True)
    business_description = models.TextField(_('Business Description'), null=True, blank=True)


    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username or self.email