# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer

from posts.models import Post

__author__ = 'joseenriquesanchezalfonso'


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('owner',)

