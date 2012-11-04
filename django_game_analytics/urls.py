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
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_game_analytics.views.home', name='home'),
    # url(r'^django_game_analytics/', include('django_game_analytics.foo.urls')),

    url(r'^open/(?P<game_name>\w+)/$','game_analytics.views.open'),
    url(r'^close/(?P<game_name>\w+)/(?P<session_id>\w+)/$','game_analytics.views.close'),
    url(r'^event/(?P<game_name>\w+)/(?P<session_id>\w+)/(?P<category>\w+)/(?P<name>\w+)/$','game_analytics.views.event'),



    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
