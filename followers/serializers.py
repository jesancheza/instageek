# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

__author__ = 'joseenriquesanchezalfonso'


class RelationshipUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
