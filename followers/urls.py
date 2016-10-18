# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from followers.views import FollowingViewSet, FollowViewSet

__author__ = 'joseenriquesanchezalfonso'

router = SimpleRouter()
router.register(r'following', FollowingViewSet, base_name='following')
router.register(r'follow', FollowViewSet)

urlpatterns = router.urls

