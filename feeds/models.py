from django.db import models


# Create your models here.
class Source(models.Model):
    name = models.CharField(max_length=255)


class Board(models.Model):
    name = models.CharField(max_length=255)
    source = models.ForeignKey(Source)


class Article(models.Model):
    topic = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    url = models.URLField()
    source = models.ForeignKey(Source)
    board = models.ForeignKey(Board)
    publish_time = models.DateTimeField()
