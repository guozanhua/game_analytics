from django.db import models

# Create your models here.

class GameSession(models.Model):
    game = models.CharField(max_length=32)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ip = models.GenericIPAddressField()
    session_id = models.CharField(max_length=32)

class GameEventCategory(models.Model):
    game = models.ForeignKey(GameSession)
    name = models.CharField(max_length=32)

class GameEvent(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(GameEventCategory)
    data = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

