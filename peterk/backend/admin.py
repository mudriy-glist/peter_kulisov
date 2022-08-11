# Author: Peter Kulisov
# Copyright: Peter Kulisov <peter.kulisov@gmail.com>
# If there are any issues contact me on the email above.
#
# Version 1.0
# Date: 11/08/2022
from django.contrib import admin

from .models import Message

# Register your models here.
admin.site.register(Message)
