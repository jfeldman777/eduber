from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.postgres.fields import ArrayField

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15,default='1')
    lat = models.FloatField()
    lng = models.FloatField()
    address = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name + ' by ' + self.user.get_username()

class Subject(models.Model):
    name = models.CharField(max_length=30,blank=False, null=False, unique=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=15, default='1')
    name = models.CharField(max_length=50,blank=False, null=False)
    locations = models.ManyToManyField(Location, null=True)

    LEVELS = (
        ('0','начинающие'),('1','продолжающие'),
        ('2','продвинутые'),('3','чемпионы')
    )

    level = models.CharField(
        max_length=1,
        choices=LEVELS,
        default='0',
    )

    letter = models.TextField(max_length=250,blank=True,null=True)
    web = models.URLField(default="", blank=True, null=True)

    age = models.PositiveIntegerField(blank=True, null=True, default=10)

    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.code + ' by ' + self.user.get_username()

class Place(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=15, default='1')
    name = models.CharField(max_length=50,blank=False, null=False)

    face1 = models.ImageField(upload_to='uploads/%Y/%m/%d',
                                   blank=True,
                                   null=True,
                                   )

    face2 = models.ImageField(upload_to='uploads/%Y/%m/%d',
                                   blank=True,
                                   null=True,
                                   )

    face3 = models.ImageField(upload_to='uploads/%Y/%m/%d',
                                   blank=True,
                                   null=True,
                                   )

    location = models.ForeignKey(Location,on_delete=models.SET_NULL,null=True)
    letter = models.TextField(max_length=250,blank=True,null=True)
    web = models.URLField(default="", blank=True, null=True)

    def __str__(self):
        return self.code + ' by ' + self.user.get_username()

class Kid(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=15, default='1')
    first_name = models.CharField(max_length=15,blank=False, null=False)
    birth_date = models.DateField()

    face = models.ImageField(upload_to='uploads/%Y/%m/%d',
                                   blank=True,
                                   null=True,
                                   )

    locations = models.ManyToManyField(Location)
    letter = models.TextField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.first_name + ' by ' + self.parent.get_username()



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

    web = models.URLField(default="", blank=True, null=True)
    adm_comment = models.TextField(default="",blank=True,null=True)

    face = models.ImageField(upload_to='uploads/%Y/%m/%d',
                                       blank=True,
                                       null=True,
                                       )


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
