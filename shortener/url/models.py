from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings


class URL(models.Model):
    short_link = models.CharField(max_length=20)
    long_link = models.URLField("URL", unique=True)

    def __str__(self):
        return self.long_link
