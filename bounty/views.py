from bounty.models import ActiveBounty, ActiveBountySubmission, Bounty
from django.shortcuts import render
from .serializers import ActiveBountySerializer, ActiveBountySubmissionSerializer, BountySerializer, GetActiveBountySerializer, GetBountySerializer
from rest_framework import generics, permissions,status
from rest_framework.response import Response
import base64
from users.models import User,Profile
from django.core.files.base import ContentFile
from transport_co2 import estimate_co2
import math
# Create your views here.
class CreateBounty(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def post(self, request, *args, **kwargs):
        request.data["user"]=request.user.id
        serializer=BountySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class GetBounties(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get(self, request,*args, **kwargs):
        queryset = Bounty.objects.all()#exclude(user=request.user.id)
        serializer=GetBountySerializer(queryset,many=True)
        return Response(serializer.data)


class StartBounty(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def post(self, request, *args, **kwargs):
        request.data["user"]=request.user.id
        if(ActiveBounty.objects.filter(user=self.request.user.id,started=True).count()==Bounty.objects.get(id=request.data["bounty"])):
            return Response("Bounty full")
        serializer=ActiveBountySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetActiveBounty(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get(self, request,*args, **kwargs):
        try:
            queryset = ActiveBounty.objects.get(user=request.user.id)

            serializer=GetActiveBountySerializer(queryset)
            return Response(serializer.data)

        except ActiveBounty.DoesNotExist:
            return Response({"msg":"No Active Bounty"})
class GetAwaitingApproval(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get(self, request,*args, **kwargs):
        user_bounties = Bounty.objects.filter(user=request.user)
        submissions=[]
        for bounty in user_bounties:
            active=ActiveBounty.objects.filter(bounty=bounty.id)
            for a in active:
                try:
                    submission=ActiveBountySubmission.objects.get(activeBounty=a.id)
                    submissions.append(submission)
                except ActiveBountySubmission.DoesNotExist:
                    submission = None
                

        serializer=ActiveBountySubmissionSerializer(submissions,many=True)        
        return Response(serializer.data)


class CancelActiveBounty(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def delete(self,request):
        ActiveBounty.objects.get(user=request.user.id).delete()
        profile=Profile.objects.get(user=request.user)
        profile.balance+=500
        profile.save()
        
        return Response()
class StartActiveBounty(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def put(self, request,*args, **kwargs):

        bounty=ActiveBounty.objects.get(user=request.user.id)
        bounty.started=True
        bounty.save()
        return Response("Bounty Started")
def getTravelEmissions(distance):
    emissions={}
    emissions["car"]=estimate_co2(mode="car", distance_in_km=distance)
    emissions["transit"]=estimate_co2(mode="transit",distance_in_km=distance)
    
    #cutting 4% of a full grown tree
    percentage=emissions["car"]/1000/252
    if(percentage>1):
        percentage=math.ceil(percentage)
    emissions["car-trees"]=percentage
    percentage=emissions["transit"]/1000/252
    if(percentage>1):
        percentage=math.ceil(percentage)
    emissions["transit-trees"]=percentage

    return emissions

class SubmitActiveBounty(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def post(self, request,*args, **kwargs):
        data=request.data
        url=data["photo"]
        active=ActiveBounty.objects.get(user=request.user.id)
        image_file=ContentFile(base64.b64decode(url),name=f"submission-{active.id}.jpeg")
        print(image_file)
        data["photo"]=image_file
        active.review=True        
        
        ActiveBountySubmission.objects.create(photo=data["photo"],text=data["text"],activeBounty=active.id)
        
        active.save()
        return Response("Submitted", status=status.HTTP_201_CREATED)

class ApproveActiveBounty(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def put(self, request,*args, **kwargs):
        ActiveBountySubmission.objects.get(activeBounty=self.kwargs["id"]).delete()
        activeBounty=ActiveBounty.objects.get(id=self.kwargs["id"])
        activeBounty.completed=True
        activeBounty.save()
        b=Bounty.objects.get(id=activeBounty.bounty.id)
        profile=Profile.objects.get(user=request.data.user)
        profile.balance+=b.amount
        profile.save()
        return Response("Bounty Completed")

class DenyActiveBounty(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def put(self, request,*args, **kwargs):
        ActiveBountySubmission.objects.get(activeBounty=self.kwargs["id"]).delete()

        bounty=ActiveBounty.objects.get(id=self.kwargs["id"])
        bounty.review=False
        bounty.save()
        return Response("Bounty Denied")

