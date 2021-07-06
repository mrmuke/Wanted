from bounty.models import ActiveBounty, ActiveBountySubmission, Bounty
from django.shortcuts import render
from .serializers import ActiveBountySerializer, ActiveBountySubmissionSerializer, BountySerializer, GetActiveBountySerializer, GetBountySerializer
from rest_framework import generics, permissions,status
from rest_framework.response import Response
import base64
from users.models import User,Profile
from django.core.files.base import ContentFile
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
    def get(self, *args, **kwargs):
        queryset = Bounty.objects.all()
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
class CancelActiveBounty(generics.DestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def delete(self,request):
        profile=Profile.objects.get(user=request.user)
        profile.balance-=500
        profile.save()
        ActiveBounty.objects.get(user=request.user.id).delete()
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


class SubmitActiveBounty(generics.CreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def post(self, request,*args, **kwargs):
        data=request.data
        url=data["photo"]
        active=ActiveBounty.objects.get(user=request.user.id)
        #hompage show approval
        image_file=ContentFile(base64.b64decode(url),name=f"submission-{active.id}.jpeg")
        data["photo"]=image_file
        active.review=True
        active.save()
        serializer=ActiveBountySubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response("Bounty Submitted")

class ApproveActiveBounty(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def put(self, request,*args, **kwargs):

        activeBounty=ActiveBounty.objects.get(user=request.user.id)
        activeBounty.completed=True
        activeBounty.save()
        b=Bounty.objects.get(id=activeBounty.bounty)
        profile=Profile.objects.get(user=request.data.user)
        profile.balance+=b.amount
        profile.save()
        return Response("Bounty Completed")

class DenyActiveBounty(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def put(self, request,*args, **kwargs):

        bounty=ActiveBounty.objects.get(user=request.user.id)
        bounty.review=False
        bounty.save()
        return Response("Bounty Denied")

