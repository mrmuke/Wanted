from django.http import HttpResponse
from .serializers import WanteSerializers
from .models import Wante
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
import base64
import json

# Create your views here.
class CreateAPIView(generics.GenericAPIView):
    serializer_class = WanteSerializers
    #permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        userdata = User.objects.get(username=request.user)
        data["user"] = userdata.pk

        data_uri = data["image"]
        image_file = ContentFile(base64.b64decode(data_uri.split(',')[1]), name="Anna.jpeg")
        data["image"] = image_file
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        wante=serializer.save()
        return HttpResponse("3")
		
class GetPostDataUsingId(generics.GenericAPIView):
    serializer_class = WanteSerializers
    permission_classes = [IsAuthenticated]
	
    def post(self, request, *args, **kwargs):
        print(request.data["id"])
        data = Wante.objects.get(id=request.data["id"])
		
        returnData = {
            "name": data.name,
            "bounty": data.bounty,
            "collected": data.collected,
            "what": data.what,
            "who": data.who,
            "where": data.where,
            "why": data.why,
            "user": data.user.username,
            "image": data.image.url,
            "date": data.date.strftime("%d/%m/%Y")
        }
		
        return HttpResponse(json.dumps(returnData))

class getAmountPostData(generics.GenericAPIView):
    serializer_class = WanteSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data["pages"])
        allWante = Wante.objects.all()[:request.data["pages"]]
        arr = []
        for obj in allWante:
            serialized_obj = WanteSerializers(obj).data
            userid = serialized_obj["user"]
            serialized_obj["user"] = User.objects.get(pk=userid).username
            arr.append(serialized_obj)

        return HttpResponse(json.dumps({"data":arr}))