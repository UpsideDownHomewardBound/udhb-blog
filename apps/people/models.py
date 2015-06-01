from django.db import models


class User(models.Model):
    username = models.CharField(max_length=80)
    password = models.CharField(max_length=255)


class Friend(User):
    pass


class PhoneNumberManager(models.Manager):

    def get_or_create_from_twilio(self, number, *args, **kwargs):
        int_number = int(number)
        try:
            number_object = self.get(number=int_number)
        except PhoneNumber.DoesNotExist:
            number_object = self.create(number=int(number), *args, **kwargs)
        return number_object


class PhoneNumber(models.Model):

    objects = PhoneNumberManager()

    PHONE_TYPES = (
        (0, "mobile"),
        (1, "work"),
        (2, "home"),
    )
    number = models.IntegerField()
    type = models.IntegerField(choices=PHONE_TYPES)

    def __unicode__(self):
        return str(self.number)