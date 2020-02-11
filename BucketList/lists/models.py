from django.db import models
from django.utils import timezone

class BucketList(models.Model):
    life_todo_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


# RESTAPI test code
class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()
    # 名前を見やすくする
    def __repr__(self):
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__ 


class Entry(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
            (STATUS_DRAFT, "下書き"),
            (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
