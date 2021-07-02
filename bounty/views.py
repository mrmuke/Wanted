from bounty.models import ActiveBounty, Bounty
from django.shortcuts import render
from .serializers import ActiveBountySerializer, BountySerializer, GetActiveBountySerializer, GetBountySerializer
from rest_framework import generics, permissions,status
from rest_framework.response import Response

from users.models import User,Profile
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
        if(ActiveBounty.objects.filter(user=self.request.user.id).count()==Bounty.objects.get(id==request.data.bounty)):
            return Resposne("Bounty full")
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

        queryset = ActiveBounty.objects.get(user=request.user.id)

        serializer=GetActiveBountySerializer(queryset)
        return Response(serializer.data)

class StartActiveBounty(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def put(self, request,*args, **kwargs):

        bounty=ActiveBounty.objects.get(user=request.user.id)
        bounty.started=True
        bounty.save()
        return Response("Bounty Started")


class SubmitActiveBounty(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def put(self, request,*args, **kwargs):

        bounty=ActiveBounty.objects.get(user=request.user.id)
        bounty.review=True
        bounty.save()
        serializer=ActiveBountySubmissionSerializer(data=request.data)
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