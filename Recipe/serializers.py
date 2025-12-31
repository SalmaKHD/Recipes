from rest_framework import serializers

class ListSerializer(serializers.Serializer):
    # specify the fields for serializer input, can add validation also
    name = serializers.CharField(max_length=10)
