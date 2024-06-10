from djongo import models
from eli_website.utils import BaseModel
from cloudinary.models import CloudinaryField


class SuperHero(BaseModel, models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    image = CloudinaryField('image')
    level = models.IntegerField(choices=(
        (100, "100 Level"), (200, "200 Level"), (300, "300 Level"), (400, "400 Level"), 
        (500, "500 Level")
    ))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "SuperHeroes"


class Activity(BaseModel, models.Model):
    _id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')
    category = models.CharField(choices=(("upcoming", "Upcoming"), ("past", "Past")), max_length=10)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self) -> str:
        return self.title