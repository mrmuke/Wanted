from django.db import models
from django.contrib.auth.models import User
def nameFile(instance, filename):
    return '/'.join(['bounty_submissions',filename])
class Bounty(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amount=models.PositiveIntegerField(default=0)
	description=models.CharField(max_length=500)
	title=models.CharField(max_length=200)
	lng=models.FloatField()
	lat=models.FloatField()
	type=models.CharField(max_length=100)
	numPeople=models.PositiveSmallIntegerField(default=1)
	expiry = models.DateField()
	duration=models.PositiveSmallIntegerField(default=1)
	def __str__(self):
		return self.title


class ActiveBounty(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	bounty = models.ForeignKey(Bounty, on_delete=models.CASCADE)
	completed = models.BooleanField(default=False)
	review=models.BooleanField(default=False)
	started=models.BooleanField(default=False)

	def __str__(self):
		return self.user.email

class ActiveBountySubmission(models.Model):
	text=models.CharField(max_length=500)
	photo = models.ImageField(upload_to=nameFile,blank=True,null=True)
	activeBounty = models.ForeignKey(ActiveBounty,on_delete=models.CASCADE)
	def __str__(self):
		return self.text