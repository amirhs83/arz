from django.db import models
from django.core.validators import FileExtensionValidator


choice=(('1','forexclub'),('2','futureclub'),('3','spotclub'))


class Weblog(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    on = models.CharField(max_length = 20, 
        choices =choice , 
        default = 'forexclub')
    
    img = models.ImageField(upload_to='uploads/images',null=True)
    

class Video(models.Model):
    
    img = models.ImageField(upload_to='uploads/images',null=True)
    video = models.FileField(upload_to='uploads/videos',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    title = models.CharField(max_length=255,null=True,blank=True)
    body = models.TextField()
    
    date_uploaded = models.DateTimeField(auto_now_add=True)




class Webhook(models.Model):
    name=models.CharField(max_length=30)
    timeframe=models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name




class PompDump(models.Model):

    name=models.CharField(max_length=30)
    timeframe=models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)





class Cryptos(models.Model):
    name=models.CharField(max_length=30)
    img = models.ImageField(upload_to='uploads/images',null=True)