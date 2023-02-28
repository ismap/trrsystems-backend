from .models import Inspection

from rest_framework import serializers

class InspectionSerializer(serializers.ModelSerializer):
    inspection_create = serializers.DateTimeField(format="%d-%m-%y %I:%M", read_only=True)
    class Meta:
        model = Inspection
        fields = '__all__'