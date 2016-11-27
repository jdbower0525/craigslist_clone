from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserForm(models.Model):
    pass


class Lister(models.Model):
    user = models.OneToOneField(User, null=True)
    e_mail = models.CharField(max_length=30)
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)


class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=140)
    lister = models.ForeignKey(Lister, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Posting(models.Model):
    content = models.CharField(max_length=140)
    lister = models.ForeignKey(Lister, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
