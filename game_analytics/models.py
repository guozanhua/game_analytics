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

class Game(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name


class GameSession(models.Model):
    game = models.ForeignKey(Game)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    ip = models.IntegerField()
    session_id = models.CharField(max_length=32)

    def store_ipv4(self,ipv4_str):
        parts = ipv4_str.split('.')
        if len(parts) == 4:
            addr = \
            ( int ( parts[3] ) ) + \
            ( int ( parts[2] ) << 8 ) + \
            ( int ( parts[1] ) << 16 ) + \
            ( int ( parts[0] ) << 24 )
            self.ip = addr

    def ipv4_str(self):
        addr = ['0','0','0','0']
        addr[0] = str ( ( self.ip & (255 << 24 )) >> 24 )
        addr[1] = str ( ( self.ip & (255 << 16 )) >> 16 )
        addr[2] = str ( ( self.ip & (255 << 8 )) >> 8 )
        addr[3] = str ( self.ip & 255 )
        return addr[0]+'.'+addr[1]+'.'+addr[2]+'.'+addr[3]


    def __unicode__(self):
        return "{game}.Session.{session}@{ip}".format(\
            game=self.game.name,\
            session=self.session_id,\
            ip=self.ipv4_str())

class GameEventCategory(models.Model):
    game = models.ForeignKey(Game)
    name = models.CharField(max_length=32)

    def __unicode__(self):
        return "{game}.{category}".format(\
            game=self.game.name,\
            category=self.name)

class GameEvent(models.Model):
    session = models.ForeignKey(GameSession)
    name = models.CharField(max_length=32)
    datetime = models.DateTimeField()
    category = models.ForeignKey(GameEventCategory)
    data = models.TextField(null=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    def __unicode__(self):
        return "{game}.{session}.{category}.{event}".format(\
            game=self.session.game.name,\
            session=self.session.session_id,\
            category=self.category.name,\
            event=self.name)


