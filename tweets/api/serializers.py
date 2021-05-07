from rest_framework import serializers
from accounts.api.serializers import UserSerializerForTweet
from tweets.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    user = UserSerializerForTweet()

    class Meta:
        model = Tweet
        fields = ('id', 'user', 'created_at', 'content')
