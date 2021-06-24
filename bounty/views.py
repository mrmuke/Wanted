from bounty.models import ActiveBounty, Bounty
from django.shortcuts import render
from .serializers import ActiveBountySerializer, BountySerializer, GetActiveBountySerializer, GetBountySerializer
from rest_framework import generics, permissions,status
from rest_framework.response import Response

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
        serializer=ActiveBountySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetActiveBounties(generics.ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def get(self, request,*args, **kwargs):

        queryset = ActiveBounty.objects.filter(user=request.user.id)

        serializer=GetActiveBountySerializer(queryset,many=True)
        return Response(serializer.data)

class StartWorkingActive(generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def put(self, request,*args, **kwargs):

        bounty=ActiveBounty.objects.get(user=request.user.id,bounty=request.data["bounty"])
        bounty.started=True
        bounty.save()
        return Response("Bounty Started")