__author__ = 'Matthew Hughes (@argylelabcoat)'
__license__ = '''
This file is part of game_analytics.

    game_analytics is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    game_analytics is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with game_analytics.  If not, see <http://www.gnu.org/licenses/>.
'''
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

