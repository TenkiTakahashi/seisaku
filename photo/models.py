from django.db import models


class Tweet(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    point = models.IntegerField()
