from django.db import models

# from ckeditor_uploader.fields import RichTextUploadingField

from datetime import datetime

# from django.db.models import Sum
# from django.db.models.functions import Coalesce

from django.core.validators import MinValueValidator
from django.db.models import ForeignKey
from django.urls import reverse

from django.core.cache import cache

from django.utils.translation import gettext_lazy as _


class Coords(models.Model):

    latitude = models.IntegerField(default=0)
    longitude = models.FloatField()
    height = models.FloatField()

class Level(models.Model):
    level_1A = '1A'
    level_1B = '1B'
    level_2A = '1A'
    level_2B = '2B'
    level_3A = '3A'
    level_3B = '3B'

    LEVEL_CHOICES = (
        (level_1A, '1A'),
        (level_1B, '1Б'),
        (level_2A, '2A'),
        (level_2B, '2Б'),
        (level_3A, '3A'),
        (level_3B, '3Б'),
    )

    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES)


class User(models.Model):

    email = models.EmailField(max_length=64, unique=True)
    fam = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    otc = models.CharField(max_length=120)
    phone = models.CharField(max_length=64)


class Pereval(models.Model):

    beauty_title = models.CharField(max_length=64, unique=True)
    title = models.CharField(max_length=120)
    other_titles = models.CharField(max_length=120)
    connect = models.CharField(max_length=120)
    add_time = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = ForeignKey(Coords, on_delete=models.CASCADE)
    level = ForeignKey(Level, on_delete=models.CASCADE)


class Images(models.Model):

    data = models.CharField(max_length=120)
    title = models.URLField(max_length=120)
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, blank=True, null=True, related_name='images')