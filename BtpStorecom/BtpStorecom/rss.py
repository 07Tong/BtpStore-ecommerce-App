from django.conf import settings
from django.contrib.syndication.views import Feed
from django.shortcuts import reverse

from shop import models

class BaseFeed(Feed):
    author_email = 'contact.btpstorecom@gmail.com'
    author_name = 'BtpStorecom'
    language = 'fr'

class LatestBuildingElectricite(BaseFeed):
    link = '/collection/grosoeuvre/electricite'

    def items(self):
        return models.ProductCollection.collection_manager.active_products('electricite')

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description

    def item_extra_kwargs(self, item):
        return {'price_ht': item.price_ht}
