from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.SlugField(max_length=15)
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name + ' by ' + self.user.get_username()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20,null=True, blank=True)

    ask_parent = models.BooleanField(default=False)
    ask_producer = models.BooleanField(default=False)
    ask_teacher = models.BooleanField(default=False)

    has_parent = models.BooleanField(default=False)
    has_producer = models.BooleanField(default=False)
    has_teacher = models.BooleanField(default=False)

    adm_comment = models.TextField(default="",blank=True,null=True)

    def __str__(self):
        return self.user.get_username()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Reference(models.Model):
    person_from = models.ForeignKey(User,on_delete=models.CASCADE, related_name='writer')
    person_to = models.ForeignKey(User,on_delete=models.CASCADE,related_name='hero')
    letter = models.TextField(default="",blank=True,null=True)
    written = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person_from.get_username()+'->'+self.person_to.get_username()
