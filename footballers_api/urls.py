from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^players/$', views.players_list),
    url(r'^players/(?P<player_id>\d+)$', views.players_list)
]