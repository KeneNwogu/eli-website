from rest_framework import serializers

from site_content.models import SuperHero, Activity


class SuperHeroSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = SuperHero
        fields = "__all__"


class ActivitySerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Activity
        fields = "__all__"