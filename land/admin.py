from django.contrib import admin
from .models import Profile, Reference, Location, Kid, Place, Course, Subject
from .models import Claim, Prop, Chat, Reply, Event

class ChatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Chat, ChatAdmin)


class ReplyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Reply, ReplyAdmin)

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)


class PropAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prop, PropAdmin)

class ClaimAdmin(admin.ModelAdmin):
    pass

admin.site.register(Claim, ClaimAdmin)

class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)

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

class CourseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Course, CourseAdmin)
