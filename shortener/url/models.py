from django.db import models


class URL(models.Model):
    short_link = models.CharField(max_length=20)
    long_link = models.URLField("URL", unique=True)

    def __str__(self):
        return self.long_link
