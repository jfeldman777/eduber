from django.contrib import admin

from .models import Parent, Kid
# Register your models here.

class ParentAdmin(admin.ModelAdmin):
    pass

class KidAdmin(admin.ModelAdmin):
    pass

admin.site.register(Parent, ParentAdmin)
admin.site.register(Kid, KidAdmin)
