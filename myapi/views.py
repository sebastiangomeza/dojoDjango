from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
# Create your views here.

class HeroViewSet(mixins.ListModelMixin,mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer