from concurrent.futures.process import _ThreadWakeup
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Events(models.Model):
    
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    event_photo = models.ImageField(null = True, blank = True)
    number_of_seats = models.IntegerField()
    active_or_not = models.BooleanField()

class RegisterdEvents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()

    def __str__(self) -> str:
        return self.event_id.name

class CountImage(models.Model):
    image = models.ImageField(null = False, blank = False)
    Event_name = models.CharField(max_length=100, null=True)
    count = models.IntegerField(null=True,blank=True)

    
  
