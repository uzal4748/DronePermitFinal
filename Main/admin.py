from django.contrib import admin
from . models import *

class DroneAdmin(admin.ModelAdmin):
    list_display = ('reg_id','owners','modelno','manufacturer','category','types','weight','max_takeoff')

admin.site.register(Drone, DroneAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'fname', 'lname', 'email', 'tele_no','pilot_fname','pilot_lname','pilot_email','pilot_tele_no')  # Add 'pk' (primary key) field to the list display

admin.site.register(Owner, OwnerAdmin)

class AreaAdmin(admin.ModelAdmin):
    list_display= ('district','municipality','wardno','areainsqm')

admin.site.register(Area, AreaAdmin)

class DronePermitAdmin(admin.ModelAdmin):
    list_display = ('owner', 'drone', 'area', 'purpose', 'status','date_created')
    list_filter = ('status',)
    search_fields = ('owner__fname', 'owner__lname', 'drone__modelno')

admin.site.register(DronePermit, DronePermitAdmin)