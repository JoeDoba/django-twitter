from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from tweets.models import Tweet
from tweets.api.serializers import TweetSerializer

class TweetViewSet(viewsets.GenericViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    #Check permission before getting list or creation
    def get_permissions(self):
        # Allow anyone to check the tweet list even without login
        if self.action == 'list':
            return [AllowAny()]
        # All other actions need user login
        return [IsAuthenticated()]


    def list(self, request, *args, **kwargs):
        if "user_id" not in request.query_params:
            return Response("Missing user id", status=400)
        tweets = Tweet.objects.filter(
            user_id=request.query_params['user_id']
        ).order_by('-created_at')
        serializer = TweetSerializer(tweets, many=True)
        return Response({'tweets': serializer.data})



    def create(self, request, *args, **kwargs):
        pass


