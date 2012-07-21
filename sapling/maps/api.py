from tastypie import fields
from tastypie.bundle import Bundle
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie.contrib.gis.resources import ModelResource

from models import MapData
import pages.api  # Scoped import to prevent ImportError.
from sapling.api import api


class MapResource(pages.api.PageURLMixin, ModelResource):
    page = fields.ToOneField(pages.api.PageResource, 'page')

    class Meta:
        queryset = MapData.objects.all()
        resource_name = 'map'
        detail_uri_name = 'page__name'
        filtering = {
            'page': ALL_WITH_RELATIONS,
            'points': ALL,
            'lines': ALL,
            'polys': ALL,
            'geom': ALL,
            'length': ALL,
        }


# We don't use detail_uri_name here because it becomes too complicated
# to generate pretty URLs with the historical version identifers.
# TODO: Fix this. Maybe easier now with `detail_uri_name` and the uri prep
# method.
class MapHistoryResource(ModelResource):
    page = fields.ToOneField(pages.api.PageHistoryResource, 'page')

    class Meta:
        queryset = MapData.versions.all()
        resource_name = 'map_version'
        filtering = {
            'page': ALL_WITH_RELATIONS,
            'points': ALL,
            'lines': ALL,
            'polys': ALL,
            'geom': ALL,
            'length': ALL,
        }


api.register(MapResource())
api.register(MapHistoryResource())