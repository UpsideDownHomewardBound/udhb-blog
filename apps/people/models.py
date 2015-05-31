from django.db import models


class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=255)


class Friend(User):
    pass


class PhoneNumber(models.Model):
    PHONE_TYPES = (
        (0, "mobile"),
        (1, "work"),
        (2, "home"),
    )
    number = models.IntegerField()
    type = models.IntegerField(choices=PHONE_TYPES)
    owner = models.ForeignKey(Friend)