
from .models import AccessVehicle
from inspectionsvehicle.models import Inspection

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

class InspectionSerializer(SerializerExtensionsMixin, ModelSerializer):
    class Meta:
        model = Inspection
        fields = "__all__"

class AccessControlSerializer(SerializerExtensionsMixin, ModelSerializer):
    access_date = serializers.DateTimeField(format="%d-%m-%y %I:%M", read_only=True)
    access_inspection = InspectionSerializer(required=False)
    class Meta:
        model = AccessVehicle
        fields = "__all__"

    def create(self, validated_data):
        inspection_data = validated_data.pop('access_inspection')
        access_inspection = Inspection.objects.create(**inspection_data)
        return AccessVehicle.objects.create(access_inspection=access_inspection, **validated_data)
        
