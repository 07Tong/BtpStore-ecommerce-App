from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from shop import models


class HomeSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class ShopSitemap(Sitemap):
    """Returns all the products from the shop"""
    changefreq = 'monthly'
    priority = 1
    protocol = 'https'

    def items(self):
        return ['shop']

    def location(self, view):
        return reverse(view)

class BuildingShopSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'

    def items(self):
        return ['shop_gender']

    def location(self, viewname):
        return reverse('shop_gender', args=['grosoeuvre'])

class MaterialShopSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1
    protocol = 'https'

    def items(self):
        return ['shop_gender']

    def location(self, viewname):
        return reverse('shop_gender', args=['secondoeuvre'])

class Materiaux(Sitemap):
    changefreq = 'daily'
    priority = 1
    protocol = 'https'

    def items(self):
        return models.Product.objects.filter(collection__view_name='materiaux')

    def lastmod(self, product):
        return product.last_modified

class Outillage(Sitemap):
    changefreq = 'daily'
    priority = 1
    protocol = 'https'

    def items(self):
        return models.Product.objects.filter(collection__view_name='outillage')

    def lastmod(self, product):
        return product.last_modified

class Plomberie(Sitemap):
    changefreq = 'daily'
    priority = 1
    protocol = 'https'

    def items(self):
        return models.Product.objects.filter(collection__view_name='plomberie')

    def lastmod(self, product):
        return product.last_modified

class Electricite(Sitemap):
    changefreq = 'daily'
    priority = 1
    protocol = 'https'

    def items(self):
        return models.Product.objects.filter(collection__view_name='electricite')

    def lastmod(self, product):
        return product.last_modified

class LegalSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.2
    protocol = 'https'

    def items(self):
        return ['cgv', 'cgu', 'confidentialite']

    def location(self, item):
        return reverse(item)

class WhoAreWeSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.4
    protocol = 'https'

    def items(self):
        return ['who_are_we']

    def location(self, item):
        return reverse(item)

class CustomerCareSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.2
    protocol = 'https'

    def items(self):
        return ['customer_care', 'contact_us']

    def location(self, item):
        return reverse(item)

SITEMAPS = {
    'HomeSitemap': HomeSitemap,
    'LegalSitemap': LegalSitemap,
    'ShopGenderSitemap': BuildingShopSitemap,
    'MaterialShopSitemap': MaterialShopSitemap,
    'WhoAreWeSitemap': WhoAreWeSitemap,
    'CustomerCareSitemap': CustomerCareSitemap,

    'Materiaux': Materiaux,
    'Outillages': Outillage,
    'Plomberie': Plomberie,
    'Electricite': Electricite
}
