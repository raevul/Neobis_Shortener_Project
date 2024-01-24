from django.db import models


class Url(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField("Url", unique=True)

    def __str__(self):
        return self.short_url
