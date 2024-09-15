
from django.db import models
from django.contrib.auth.models import User







class otpcode(models.Model):
    code=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    


