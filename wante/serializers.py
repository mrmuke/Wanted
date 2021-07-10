from .models import Wante
from rest_framework import serializers

class WanteSerializers(serializers.ModelSerializer):
    class  Meta:
        model=Wante
        fields='__all__'