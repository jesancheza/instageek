# -*- coding: utf-8 -*-
from easy_thumbnails.files import generate_all_aliases

__author__ = 'joseenriquesanchezalfonso'


def generate_responsive_images(post):
    generate_all_aliases(post.image, True)

