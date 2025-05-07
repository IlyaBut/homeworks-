from tkinter.constants import CASCADE

from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=150, null= False)
    description = models.CharField(max_length= 250, null= True)

class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, related_name='measurement', on_delete= models.CASCADE)
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField( auto_now_add = True) # Время при создании
    updated_at = models.DateTimeField(auto_now = True) # Время последнего обновления.