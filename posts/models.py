from django.db import models

from django.conf import settings


class Posts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               default=True,
                               null=True,
                               on_delete=models.CASCADE,
                               related_name='posts')
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

class Tag(models.Model):
    title = models.CharField(max_length=100)
    posts = models.ManyToManyField(Posts)
