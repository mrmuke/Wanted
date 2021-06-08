from django.db import models
from django.contrib.auth.models import User

class Bounty(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    title=models.CharField(max_length=200)
    lng=models.DecimalField(max_digits=9, decimal_places=6)
    lat=models.DecimalField(max_digits=9, decimal_places=6)
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.title


        
