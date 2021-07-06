from bounty.serializers import ActiveBountySerializer
from django.contrib import admin
from .models import ActiveBounty, ActiveBountySubmission
from users.models import Profile
# Register your models here.
admin.site.register(ActiveBounty)
admin.site.register(ActiveBountySubmission)
admin.site.register(Profile)