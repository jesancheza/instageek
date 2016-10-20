# -*- coding: utf-8 -*-
from django.conf import settings
__author__ = 'joseenriquesanchezalfonso'


DEFAULT_IMAGE_SIZE = getattr(settings, 'DEFAULT_IMAGE_SIZE', (500, 500))
DEFAULT_IMAGE_OPTIONS = getattr(settings, 'DEFAULT_IMAGE_OPTIONS', {"size": DEFAULT_IMAGE_SIZE, "crop": True})
