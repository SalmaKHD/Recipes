from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Recipe import models
from Recipe.models import UserProfile


class ListSerializer(serializers.Serializer):
    # specify the fields for serializer input, can add validation also
    # specify fields directly
    name = serializers.CharField(max_length=10)

class ProfileSerializer(ModelSerializer):
    class Meta:
        # define model for the serializer
        model=UserProfile
        fields=('id', 'email', 'name', 'password')
        extra_kwargs= {
            'password': {
                'write_only': True,
                'style': {'input': 'password'}
            }
        }

        def create(self, validated_data):
            # override function used for creating object
            user = models.UserProfile.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                name=validated_data['name']
            )

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        # id created by default for each row
        # user_profile is a foreign key
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }




