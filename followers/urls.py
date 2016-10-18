# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from followers.views import FollowingViewSet

__author__ = 'joseenriquesanchezalfonso'

router = SimpleRouter()
router.register(r'following', FollowingViewSet, base_name='following')

urlpatterns = router.urls

