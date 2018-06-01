from django.db import models

# Create your models here.
class Parent(models.Model):
    first_name = models.CharField(max_length = 15, blank = False)
    otch = models.CharField(max_length = 15, blank = False)
    last_name = models.CharField(max_length = 20, blank = False)
    address = models.CharField(max_length = 50, blank=True, null = True)
    phone = models.CharField(max_length = 20, blank = False)

    lat = models.FloatField(default=59.93863)
    lng = models.FloatField(default=30.31413)

    def __str__(self):
        return self.first_name + " " + self.otch + " " + self.last_name

class Kid(models.Model):
    name = models.CharField(max_length = 15, blank = False)
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    face = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, null=True)
    def __str__(self):
        return self.name + " " + self.parent.last_name + " "
