from django.db import models

class BaseModel(models.Model):

    "Base Model class possessing useful timestamps and a utility method and function."

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def new(cls, **kwargs) -> models.Model:
        "Create and save a new model instance"
        ins = cls(**kwargs)
        ins.save()
        return ins

    def update(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
        self.save()
        self.refresh_from_db()