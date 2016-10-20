from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Post(models.Model):

    owner = models.ForeignKey(User)
    description = models.TextField()
    image = ThumbnailerImageField(resize_source={"size": (500, 500)})
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
