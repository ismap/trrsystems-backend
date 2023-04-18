from .models import Inspection
from accessvehicle.models import AccessVehicle


from rest_framework import serializers

class InspectionSerializer(serializers.ModelSerializer):
    inspection_create = serializers.DateTimeField(format="%d-%m-%y %I:%M", read_only=True)
    class Meta:
        model = Inspection
        fields = '__all__'

class AccessControlSerializer(serializers.ModelSerializer):
    access_date = serializers.DateTimeField(format="%d-%m-%y %I:%M", read_only=True)
    access_inspection = InspectionSerializer()
    class Meta:
        model = AccessVehicle
        fields =  ["id","access_date","access_control","access_truck","access_trailer","access_inspection"]
    def update(self, instance, validated_data):
        access_inspection = validated_data.pop('access_inspection', None)
        if access_inspection:
            inspection_serializer = InspectionSerializer(instance=instance.access_inspection, data=access_inspection)
            inspection_serializer.is_valid(raise_exception=True)
            inspection_serializer.save()

        instance = super().update(instance, validated_data)
        return instance