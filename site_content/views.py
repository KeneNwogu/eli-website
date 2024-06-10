from rest_framework.generics import ListAPIView

from site_content.models import SuperHero, Activity
from site_content.serializers import SuperHeroSerializer, ActivitySerializer


class SuperHeroView(ListAPIView):
    serializer_class = SuperHeroSerializer
    queryset = SuperHero.objects.all()


class ActivityView(ListAPIView):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()