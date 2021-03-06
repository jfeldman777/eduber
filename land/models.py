from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class QPage(models.Model):
    hide = models.BooleanField(default=False)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    letter = models.TextField(max_length=250,blank=True,null=True)
    img = models.ImageField(upload_to='uploads/%Y/%m/%d',
                                       blank=True,
                                       null=True,
                                       )
    def __str__(self):
        return self.code +' by ' + self.user.get_username()

class QLine(models.Model):
    hide = models.BooleanField(default=False)
    page = models.ForeignKey(QPage,on_delete=models.CASCADE)
    letter = models.TextField(max_length=250,blank=True,null=True)
    img = models.ImageField(upload_to='uploads/%Y/%m/%d',
                                       blank=True,
                                       null=True,
                                       )
    line_number = models.PositiveIntegerField()

    code = models.CharField(max_length=30,default="?")

    LEVELS = (
        ('1',_('essay')),
        ('2',_('yes-no')),('3',_('options'))
    )

    type = models.CharField(
        max_length=1,
        choices=LEVELS,
        default='2',
    )

    def __str__(self):
        return self.line_number +' of ' + self.page

class QOption(models.Model):
    line = models.ForeignKey(QLine,on_delete=models.CASCADE)
    letter = models.TextField(max_length=250)

    option_number = models.PositiveIntegerField()

    def __str__(self):
        return self.option_number +' of ' + self.line

class Chat(models.Model):
    person_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first')
    person_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='second')
    subject = models.CharField(max_length=20)
    letter = models.TextField(max_length=250,blank=True,null=True)
    started = models.DateTimeField(auto_now_add=True)
    obj_id = models.PositiveIntegerField(blank=True, null=True)

class Reply(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    letter = models.TextField(max_length=250,blank=True,null=True)
    written = models.DateTimeField(auto_now_add=True)
    from_starter = models.BooleanField(default=False)


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
    locations = models.ManyToManyField(Location)

    LEVELS = (
        ('0',_('beginners')),('1',_('intermediate')),
        ('2',_('advanced')),('3',_('champions'))
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

    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
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
    interest = models.TextField(max_length=250,blank=True,null=True)

    def __str__(self):
        return self.first_name + ' by ' + self.parent.get_username()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20,null=True, blank=True)

    ask_justme = models.BooleanField(default=False)
    ask_parent = models.BooleanField(default=False)
    ask_producer = models.BooleanField(default=False)
    ask_teacher = models.BooleanField(default=False)

    has_justme = models.BooleanField(default=False)
    has_parent = models.BooleanField(default=False)
    has_producer = models.BooleanField(default=False)
    has_teacher = models.BooleanField(default=False)

    web = models.URLField(default="", blank=True, null=True)
    adm_comment = models.TextField(default="",blank=True,null=True)

    face = models.ImageField(upload_to='uploads/%Y/%m/%d',
                                       blank=True,
                                       null=True,
                                       )
    pref_kid = models.ForeignKey(Kid, on_delete=models.SET_NULL, blank=True, null = True)
    pref_addr = models.ForeignKey(Location, on_delete = models.SET_NULL, blank=True, null = True)

    letter = models.TextField(max_length=250,blank=True,null=True)

    friends = models.ManyToManyField(User, blank=True, related_name = 'friend')

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


class Prop(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    CHOICES = [('B',_('babysitter')),('R',_('tutor'))
        ,('C',_('net counselor'))
    ]
    choices = models.CharField(
        max_length=1,
        choices=CHOICES,
        default='B',
    )
    location = models.ForeignKey(Location,on_delete=models.SET_NULL,
        blank=True,null=True
        )
    subjects = models.ManyToManyField(Subject, blank=True)
    letter = models.TextField(max_length=250,blank=True,null=True)
    hide =models.BooleanField(default=False)

    def __str__(self):
        return self.get_choices_display() +'('+str(self.pk)+')' +' by ' + self.user.get_username()

class Claim(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    CHOICES = [('B',_('babysitter')),('R',_('tutor')),
                ('C',_('net counselor')),
                ('T',_('target group')),('D',_('general development group'))]
    choices = models.CharField(
        max_length=1,
        choices=CHOICES,
        default='B',
    )
    kid = models.ForeignKey(Kid,on_delete=models.SET_NULL,null=True)
    location = models.ForeignKey(Location,on_delete=models.SET_NULL,
        blank=True,null=True)
    subjects = models.ManyToManyField(Subject, blank=True)
    letter = models.TextField(max_length=250,blank=True,null=True)

    hide =models.BooleanField(default=False)

    def __str__(self):
        return self.get_choices_display() +'('+str(self.pk)+')' +' by ' + self.user.get_username()

class Event(models.Model):
    hide =models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,null=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    letter = models.TextField(max_length=250,blank=True,null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    page1 = models.ForeignKey(QPage, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.code + ' by ' + self.user.get_username()

class Invite(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    LEVELS = (
        ('0',_('unknown')),('1',_('remember')),
        ('2',_('watching')),('3',_('participating'))
    )

    status = models.CharField(
        max_length=1,
        choices=LEVELS,
        default='0',
    )

    page1_done = models.BooleanField(default=False)

    def __str__(self):
        return self.get_status_display() +' ( '+str(self.event)+' ) ' +' for ' + self.user.get_username()


class APage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(QPage,on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    letter = models.TextField(max_length=1000,blank=True,null=True)
    written = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.page)+ ' at ' +str(self.written)
