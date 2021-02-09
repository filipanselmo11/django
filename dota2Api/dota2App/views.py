from rest_framework import viewsets, generics
from dota2App.models import Heroi, Item
from dota2App.serializer import HeroiSerializer, ItemSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class HeroiViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Herois"""
    queryset = Heroi.objects.all()
    serializer_classs = HeroiSerializer()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ItemViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Items"""
    queryset = Item.objects.all()
    serializer_classs = HeroiSerializer()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]