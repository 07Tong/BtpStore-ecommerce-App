"""
URL configuration for BtpStorecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from BtpStorecom import sitemaps, views
from BtpStorecom import rss

customer_cart_patterns = [
    # path('orders', TemplateView.as_view(template_name='others/faq/orders.html'), name='customer_care_orders'),
    # path('delivery', TemplateView.as_view(template_name='others/faq/delivery.html'), name='customer_care_delivery'),
    # path('returns', TemplateView.as_view(template_name='others/faq/returns.html'), name='customer_care_returns'),
    path('contact-us', TemplateView.as_view(template_name='others/faq/contact.html'), name='contact_us'),
    path('', views.CustomerServiceView.as_view(), name='customer_care'),

]

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps.SITEMAPS}, name='django.contrib.sitemaps.views.sitemap'),

    re_path(r'^who-we-are$', TemplateView.as_view(template_name='pages/legal/who_are_we.html'), name='who_are_we'),

    path('customer-care/<page_name>/', views.CustomerServiceView.as_view(), name='customer_care_additional_pages'),
    path('customer-care/', include(customer_cart_patterns)),
    
    re_path(r'^conditions-generales-utilisation$', views.CGU.as_view(), name='cgu'),
    re_path(r'^conditions-generales-ventes$', views.CGV.as_view(), name='cgv'),
    re_path(r'^confidentialite-et-cookies$', views.Confidentialite.as_view(), name='confidentialite'),
    
    re_path(r'^subscribe/', views.subscribe_user, name='subscribe_user'),

    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),

    re_path(r'^$', views.HeroView.as_view(), name='home'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom error pages
handler404 = 'BtpStorecom.views.handler404'
handler500 = 'BtpStorecom.views.handler500'
