from django.db import models


class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=255)


class Friend(User):
    pass


class PhoneNumberManager(models.Manager):

    def get_or_create_from_twilio(self, number, *args, **kwargs):
        number_object = PhoneNumber.objects.get_or_create_from_twilio(number=number, *args, **kwargs)
        return number_object


class PhoneNumber(models.Model):

    objects = PhoneNumberManager()

    PHONE_TYPES = (
        (0, "mobile"),
        (1, "work"),
        (2, "home"),
    )
    number = models.CharField(max_length=25)
    type = models.IntegerField(choices=PHONE_TYPES)

    def __unicode__(self):
        return str(self.number)