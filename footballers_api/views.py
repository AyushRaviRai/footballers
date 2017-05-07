# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Footballers
import json
from pprint import pprint
from django.core import serializers
from .serializers import FootballersSerializer

# Create your views here.

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		apiResponse = {
			'status' : 200,
			'message' : '',
			'response' : data,
			'response_time' : 2312312
		}

		content = JSONRenderer().render(apiResponse)

		kwargs['content-type'] = 'application/json'
		super(JSONResponse, self).__init__(content, kwargs)

def players_list(request, player_id=None):
	if request.method == 'GET':
		if player_id != None:
			players = Footballers.objects.all().filter(player_id=player_id);
		else :
			players = Footballers.objects.all();
		serializer = FootballersSerializer(players, many=True)
		return JSONResponse(serializer.data)

