from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Expence)
admin.site.register(CustomUser)