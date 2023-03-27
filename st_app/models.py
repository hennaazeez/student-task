from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_admin=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)



class  studentregister(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    collegename = models.CharField(max_length=1000)
    mobile = models.CharField(max_length=10, null=False)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Complaint(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(max_length=4000, blank=False, null=True)
    Time = models.DateField(auto_now=True)
    status = models.IntegerField(default=0)
    reply = models.TextField(null=True,blank=True)

class Notification(models.Model):
    sender = models.ForeignKey(Login, on_delete=models.CASCADE, null=True, related_name='sender_notification')
    recipient = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='recipient_notification')
    message = models.TextField()
    read_date = models.BooleanField(null=True,blank=True)
    sent_date = models.DateTimeField(auto_now_add=True)
    reply = models.TextField(null=True,blank=True)