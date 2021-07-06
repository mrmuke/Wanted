from .models import ActiveBounty, Bounty,ActiveBountySubmission
from rest_framework import serializers
from users.serializers import UserSerializer
class GetBountySerializer(serializers.ModelSerializer):
	user=UserSerializer()
	#started = serializers.SerializerMethodField('get_popularity')
	#def popularity(self, obj):
#		return 3#ActiveBounty.objects.filter(bounty=self.request.data.bounty,active=True).count() and started=Treu
		
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
class ActiveBountySubmissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = ActiveBountySubmission
		fields = "__all__"

class GetActiveBountySerializer(serializers.ModelSerializer):
	bounty=BountySerializer()

	class Meta:
		model = ActiveBounty
		fields = "__all__"

