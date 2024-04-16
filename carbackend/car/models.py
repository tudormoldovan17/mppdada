from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Car(models.Model):
    name = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    color = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Car)
def announce_new_car(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "cars",
            {
                "type": "car.added",  # Matches method name in consumer
                "car": Car(instance).data
            }
        )