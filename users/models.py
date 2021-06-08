from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    balance=models.PositiveIntegerField(default=0)
    bio=models.CharField(max_length=300,default="")
@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:     
        Profile.objects.create(user=instance)
    instance.profile.save()