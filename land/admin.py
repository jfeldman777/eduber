from django.contrib import admin
from .models import Profile, Reference, Location, Kid, Place

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)

class ReferenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Reference, ReferenceAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)

class KidAdmin(admin.ModelAdmin):
    pass

admin.site.register(Kid, KidAdmin)

class PlaceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)
