from .models import ActiveBounty, Bounty
from rest_framework import serializers
from users.serializers import UserSerializer
class GetBountySerializer(serializers.ModelSerializer):
	user=UserSerializer()
	class Meta:
		model = Bounty
		fields = "__all__"

class BountySerializer(serializers.ModelSerializer):
	class Meta:
		model = Bounty
		fields = "__all__"

class ActiveBountySerializer(serializers.ModelSerializer):
	class Meta:
		model = ActiveBounty
		fields = "__all__"

class GetActiveBountySerializer(serializers.ModelSerializer):
	bounty=GetBountySerializer()
	class Meta:
		model = ActiveBounty
		fields = "__all__"

