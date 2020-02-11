from django.db import models
from django.utils import timezone

class BucketList(models.Model):
    life_todo_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')