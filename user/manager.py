
from django.apps import apps
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password



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

