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

class location(models.Model):
    location_id = models.IntegerField()
    country = models.CharField(max_length=4,null=True)
    region = models.CharField(max_length=4,null=True)
    city = models.CharField(max_length=32,null=True)
    postal_code = models.CharField(max_length=16,null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    metro_code = models.IntegerField(null=True)
    area_code = models.IntegerField(null=True)

class ip_block(models.Model):
    start_ip = models.IntegerField()
    end_ip = models.IntegerField()
    location_id = models.ForeignKey(location)


