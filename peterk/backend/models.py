# Author: Peter Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 11/08/2022
from django.db import models


# Create your models here.
class Message(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    phone_number = models.IntegerField(null=True, blank=True, max_length=15)
    message = models.TextField(max_length=800)

    def __str__(self):
        return f"{self.name} {self.email}"
