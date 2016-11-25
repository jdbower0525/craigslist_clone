from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserForm(models.Model):
    pass


class Lister(models.Model):
    user = models.OneToOneField(User, null=True)

    def __str__(self):
        return str(self.id)
