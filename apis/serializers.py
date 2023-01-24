from rest_framework import serializers

class MyModelSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    id = serializers.FloatField()
    name = serializers.CharField()
    email = serializers.CharField()