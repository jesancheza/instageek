from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext as _


class PostsConfig(AppConfig):
    name = 'posts'
    verbose_name = _("Posts")
