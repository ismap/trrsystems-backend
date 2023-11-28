
from .models import AccessVehicle
from inspectionsvehicle.models import Inspection

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

class InspectionSerializer(ModelSerializer):
    inspection_create = serializers.DateTimeField(format="%d-%m-%y %I:%M", read_only=True)
    class Meta:
        model = Inspection
        fields = "__all__"

class AccessControlSerializer(ModelSerializer):
    access_date = serializers.DateTimeField(format="%d-%m-%y %I:%M", read_only=True)
    access_inspection = InspectionSerializer()
    class Meta:
        model = AccessVehicle
        fields =  ["id","access_date","access_control","access_truck","access_trailer","access_inspection"]

    def create(self, validated_data):
        inspection_data = validated_data.pop('access_inspection')
        inspection = Inspection.objects.create(**inspection_data)
        access_vehicle = AccessVehicle.objects.create(access_inspection=inspection, **validated_data)
        return access_vehicle
