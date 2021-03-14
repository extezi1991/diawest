from django.db import models

# Create your models here.
class Clent(models.Model):
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return "Пользователь %s" % (self.phone_number)

    class Meta:
        verbose_name = 'MyClient'
        verbose_name_plural = 'A lot of Clients'

