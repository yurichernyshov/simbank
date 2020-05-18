from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.Serializer):

    id = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=200)
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    hold = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.BooleanField()

    def create(self, validated_data):
        return Account.objects.create(**validated_data)

