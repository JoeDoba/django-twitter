from rest_framework import serializers
from accounts.api.serializers import UserSerializerForFriendship
from friendships.models import Friendship
from rest_framework.exceptions import ValidationError

class FollowingSerializer(serializers.ModelSerializer):
    user = UserSerializerForFriendship(source='to_user')
    created_at = serializers.DateTimeField()

    class Meta:
        model = Friendship
        fields = ('user', 'created_at')

class FollowerSerializer(serializers.ModelSerializer):
    user = UserSerializerForFriendship(source='from_user')
    created_at = serializers.DateTimeField()

    class Meta:
        model = Friendship
        fields = ('user', 'created_at')

class FriendshipSerializer(serializers.ModelSerializer):
    from_user = UserSerializerForFriendship()
    to_user = UserSerializerForFriendship()

    class Meta:
        model = Friendship
        fields = ('from_user', 'to_user')

class FriendshipSerializerForCreate(serializers.ModelSerializer):
    from_user = serializers.IntegerField()
    to_user = serializers.IntegerField()

    class Meta:
        model = Friendship
        fields = ('from_user', 'to_user')

    def validate(self, attrs):
        if attrs['from_user'] == attrs['to_user']:
            raise ValidationError({
                'message': 'from_user_id and to_user_id should be different'
            })
        return attrs

    def create(self, validated_data):
        from_user_id = validated_data['from_user']
        to_user_id = validated_data['to_user']
        return Friendship.objects.create(
            from_user_id=from_user_id,
            to_user_id=to_user_id,
        )