from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import action
from friendships.models import Friendship
from friendships.api.serializers import (
    FollowingSerializer,
    FollowerSerializer,
    #FriendshipSerializerForCreate,
)


class FriendShipViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()

    @action(methods=['GET'], detail=True, permission_classes=[AllowAny])
    def followers(self, request, pk):
        friendships = Friendship.objects.filter(to_user_id=pk).order_by('-created_at')
        serializer = FollowerSerializer(friendships, many=True)
        return Response(
            {
                'followers': serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    @action(methods=['GET'], detail=True, permission_classes=[AllowAny])
    def following(self, request, pk):
        friendships = Friendship.objects.filter(from_user_id=pk).order_by('-created_at')
        serializer = FollowingSerializer(friendships, many=True)
        return Response(
            {
                'following': serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def follow(self):
        pass

    def unfollow(self):
        pass

    def list(self, request):
        return Response({'message': 'this is from friendships'})
