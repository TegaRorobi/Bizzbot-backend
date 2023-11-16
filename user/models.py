from django.db import models
from django.apps import apps
from django.contrib.auth.models import UserManager, AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext as _


class UserManager(UserManager):
    def _create_user(self, username=None, email=None, password=None, **extra_fields):

        if email is None:
            raise ValueError("Email must be set!")
        if password is None:
            raise ValueError("Password must be set!")

        email = self.normalize_email(email)

        if username is not None:
            GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
            username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        return super().create_superuser(username=username, email=email, password=password, **extra_fields)
    
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        return super().create_superuser(username=username, email=email, password=password, **extra_fields)


class User(AbstractUser):

    full_name = models.CharField(_('Full Name'), max_length=200, null=True, blank=True)
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[UnicodeUsernameValidator()],
        error_messages={"unique": _("A user with that username already exists."),},
        null=True, 
        blank=True
    )
    email = models.EmailField(_('Email Address'), unique=True)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username or self.email