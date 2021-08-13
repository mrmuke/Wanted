from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class Wante(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name=models.CharField(max_length=200)
    bounty=models.IntegerField()
    collected=models.IntegerField(default=0)
    who=models.CharField(max_length=1000)
    what=models.CharField(max_length=1000)
    where=models.CharField(max_length=1000)
    why=models.CharField(max_length=1000)
    date=models.DateField()
    theme=models.CharField(max_length=1000)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    