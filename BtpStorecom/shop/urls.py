
from django.urls import include, path,re_path

from shop import views

cartpatterns = [
    re_path(r'^success$', views.CartSuccessView.as_view(), name='success'),
    re_path(r'^payment/process$', views.ProcessPayment.as_view(), name='payment_process'),
    re_path(r'^payment$', views.PaymentView.as_view(), name='payment'),
    re_path(r'^shipment$', views.ShipmentView.as_view(), name='shipment'),
    re_path(r'^alter/(?P<pk>\d+)/(?P<method>(add|reduce))$', views.alter_item_quantity, name='alter_quantity'),
    re_path(r'^(?P<pk>\d+)/delete$', views.delete_product_from_cart, name='delete_from_cart'),
    re_path(r'^coupon-add$', views.apply_coupon, name='add_coupon'),
    re_path(r'^no-cart$', views.EmptyCartView.as_view(), name='no_cart'),
    re_path(r'^$', views.CheckoutView.as_view(), name='checkout'),
]

urlpatterns = [
    path('cart/', include(cartpatterns)),

    re_path(r'^lookbook$', views.LookBookView.as_view(), name='lookbook'),
    re_path(r'^search$', views.SearchView.as_view(), name='search'),

    re_path(r'^private/(?P<pk>\d+)/(?P<slug>[a-z\-]+)$', views.PrivateProductView.as_view(), name='private'),
    re_path(r'^preview/(?P<pk>\d+)/(?P<slug>[a-z\-]+)$', views.PreviewProductView.as_view(), name='preview'),
    re_path(r'^special-offer/(?P<pk>\d+)/(?P<product_reference>[a-z]+)/$', views.SpecialOfferView.as_view(), name='special_offer'),
    
    re_path(r'^collections/(?P<gender>(grosoeuvre|secondoeuvre))/(?P<collection>[a-z]+)/(?P<pk>\d+)/(?P<slug>[a-z\-]+)$', views.ProductView.as_view(), name='product'),
    re_path(r'^collections/(?P<gender>(grosoeuvre|secondoeuvre))/(?P<collection>[a-z]+)$', views.ProductsView.as_view(), name='collection'),
    re_path(r'^collections/(?P<gender>(grosoeuvre|secondoeuvre))$', views.ShopGenderView.as_view(), name='shop_gender'),

    re_path(r'^$', views.IndexView.as_view(), name='shop')
]
