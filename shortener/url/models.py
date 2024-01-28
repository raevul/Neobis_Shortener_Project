from django.db import models


class URL(models.Model):
    long_link = models.URLField("URL")
    short_link = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return self.long_link
