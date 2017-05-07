# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.

class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None,)

class AboutPageView(TemplateView):
	# Another way loading default GET request page
	template_name = 'about.html'

class ListFootballers(DetailView):
	def get(self, request, **kwargs):
		print 'kwargs %s' % repr(kwargs)
		# Hit Footballers Api to get data
		players = requests.get('http://localhost:8000/api/players/')
		apiResponse = players.json()
		return render(request, 'list_footballers.html', {
			'data' : apiResponse['response']
		})

class FootballerDetails(DetailView):
	def get(self, request, **kwargs):
		player = kwargs['player']
		playerInformation = requests.get('http://localhost:8000/api/players/' . player)
		return render(request, 'footballer_details.html', {
			'player_id' : player
		})



