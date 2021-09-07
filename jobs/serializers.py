
from rest_framework import serializers

from .models import Follower

class FollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follower
        fields = ['id', 'email']
