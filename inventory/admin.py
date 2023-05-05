from django.contrib import admin

from .models import Bus, BusRoute, Driver, Seat

# Register your models here.

admin.site.register(Driver)
admin.site.register(Bus)
admin.site.register(BusRoute)
admin.site.register(Seat)
