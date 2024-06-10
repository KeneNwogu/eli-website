from django.contrib import admin

from .models import SuperHero, Activity

admin.site.register([SuperHero, Activity])
