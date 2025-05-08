from rest_framework import serializers
from measurement.models import Sensor, Measurement
# TODO: опишите необходимые сериализаторы

# Сериализатор Sensor.
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


# Сериализатор Measurement.
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at', 'updated_at']

# Сериализатор SensorDetail.
class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
