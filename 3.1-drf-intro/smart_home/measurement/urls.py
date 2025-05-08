from django.urls import path, include
from measurement.views import SensorView, UpdateSensorView, MeasurementView
from rest_framework.routers import DefaultRouter




urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()), # Чек всех датчиков+добавление
    path('sensors/<pk>/', UpdateSensorView.as_view(), name = 'sensor-update'), # Обновление датчика
    path('measurements/', MeasurementView.as_view()), # Добавление измерения
]
