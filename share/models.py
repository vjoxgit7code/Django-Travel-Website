from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

class person(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="photos")
    dess = models.TextField(default='Your Default Value Here')


