# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.core.serializers import serialize
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView
from measurement.models import Sensor, Measurement
from rest_framework.response import Response

from .serializers import MeasurementSerializer, SensorDetailSerializer

# Получить список датчиков/создать датчик.
# class SensorsListCreateView(ListCreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         serializer = SensorDetailSerializer(sensors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = SensorDetailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




