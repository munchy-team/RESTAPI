from rest_framework import serializers
from .models import MucnhyTest

class MunchySeriallizer(serializers.ModelSerializer):

    class Meta:
        model = MucnhyTest
        fields = ('id', 'munchy' )