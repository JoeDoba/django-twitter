from rest_framework import serializers
from newsfeeds.models import NewsFeed
from accounts.api.serializers import UserSerializer
from tweets.api.serializers import  TweetSerializer

class NewsFeedSerializer(serializers.ModelSerializer):
    tweet = TweetSerializer()

    class Meta:
        model=NewsFeed
        fields=['id', 'tweet']