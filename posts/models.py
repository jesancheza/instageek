# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Post(models.Model):

    owner = models.ForeignKey(User)
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    image_resized = models.BooleanField(_("Image Resized"), default=False)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
