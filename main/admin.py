from django.contrib import admin

# Register your models here.
from.models import *
admin.site.register(
    [Talaba, Muallif, Kitob, Admin, Record
])