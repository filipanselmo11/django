from rest_framework import serializers
from escola.models import Heroi, Item

class HeroiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroi
        fields = ['id', 'nome', 'descricao']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'nome', 'descricao']