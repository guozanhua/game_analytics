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
from django.http import HttpResponse
import uuid
from datetime import datetime
import json
from models import *
# Create your views here.
def index(request):
    return HttpResponse("I should display some API help here.")

def open(request,game_name):
    game = Game.objects.get(name=game_name)
    session = GameSession()
    session.session_id = uuid.uuid4().hex
    session.game = game
    session.store_ipv4(request.META["REMOTE_ADDR"])
    session.start_time = datetime.utcnow()
    session.end_time = datetime(1970,1,1,12,0,0,0)
    session.save()
    return HttpResponse(session.session_id)

def close(request,game_name,session_id):
    game = Game.objects.get(name=game_name)
    if game :
        session = GameSession.objects.get(session_id=session_id,game=game)
        if session:
            session.end_time = datetime.utcnow()
            session.save()
            return HttpResponse("True")
    return HttpResponse("False")

def event(request,game_name,session_id,category,name):
    game = Game.objects.get(name=game_name)
    if game :
        event = GameEvent()
        event.category = GameEventCategory.objects.get(name=category,game=game)
        event.session = GameSession.objects.get(session_id=session_id)
        event.name = name
        event.datetime = datetime.utcnow()
        if event.category and event.session and event.name:
            if request.body:
                post_data = json.loads(request.body)
            else:
                post_data = {}
            if "data" in post_data:
                event.data = post_data["data"]
            else:
                event.data = ""
            if "x" in post_data:
                event.x = float(event["x"])
            else:
                event.x = 0.0
            if "y" in post_data:
                event.y = float(event["y"])
            else:
                event.y = 0.0
            if "z" in post_data:
                event.z = float(event["z"])
            else:
                event.z = 0.0
            event.save()
            return HttpResponse("True")
    return HttpResponse("False")

