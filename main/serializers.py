from rest_framework import serializers

class CountSerializer(serializers.Serializer):
    count = serializers.IntegerField(required=True, min_value=0)
    