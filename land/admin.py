from django.contrib import admin
from .models import Profile, Reference

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)

class ReferenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Reference, ReferenceAdmin)
