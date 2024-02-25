from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from django_filters import rest_framework as djangofilters

from players.permissions import IsAuthenticated, IsPelada, IsOwnerPelada


class FilteringAndOrderingMixin(object):
    """Default settings for filtering """
    filter_backends = (
        djangofilters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class IsPeladaMixin(object):
    permission_classes = (
        IsPelada,
    )


class IsOwnerPeladaMixin(object):
    permission_classes = (
        IsOwnerPelada,

    )

class IsAuthenticatedMixin(object):
    permission_classes = (
        IsAuthenticated,
    )
