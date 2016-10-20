# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet

__author__ = 'joseenriquesanchezalfonso'


router = SimpleRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
