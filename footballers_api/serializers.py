from models import Footballers
from rest_framework import serializers

class FootballersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Footballers
		fields = ('player_id', 'name', 'age', 'club', 'birth_date', 'rating')