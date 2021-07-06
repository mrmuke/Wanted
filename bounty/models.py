from django.db import models
from django.contrib.auth.models import User

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

class ActiveBountySubmission(models.Model):
	text=models.CharField(max_length=500)
	photo = models.ImageField(upload_to='bounty_submission/')

class ActiveBounty(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	bounty = models.ForeignKey(Bounty, on_delete=models.CASCADE)
	completed = models.BooleanField(default=False)
	review=models.BooleanField(default=False)
	started=models.BooleanField(default=False)
	submission = models.ForeignKey(ActiveBountySubmission,null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.email

