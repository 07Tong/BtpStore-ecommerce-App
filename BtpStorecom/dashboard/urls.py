from django.urls import include, path,re_path

from dashboard import views, api_views

app_name='dashboard'



apipatterns = [
    re_path(r'charts/(?P<name>[a-zA-Z]+)$', api_views.ChartsView.as_view(), name='chart')
]

collectionpatterns = [
    re_path(r'^(?P<pk>\d+)/update$', views.UpdateCollectionView.as_view(), name='update'),
    re_path(r'^new$', views.CreateCollectionView.as_view(), name='create'),
    re_path(r'^$', views.CollectionsView.as_view(), name='home'),
]

couponspatterns = [
    re_path(r'^(?P<pk>\d+)/activate$', views.activate_coupon, name='activate'),
    re_path(r'^(?P<pk>\d+)/update$', views.UpdateCouponsView.as_view(), name='update'),
    re_path(r'^new$', views.CreateCouponsView.as_view(), name='create'),
    re_path(r'^$', views.CouponsView.as_view(), name='home'),
]

imagespatterns = [
    re_path(r'^(?P<pk>\d+)/associate-image$', views.associate_images, name='associate'),

    re_path(r'^new', views.create_images, name='create'),
    re_path(r'^(?P<pk>\d+)$', views.ImageView.as_view(), name='update'),
    re_path(r'^$', views.ImagesView.as_view(), name='home'),
]

productpatterns = [
    re_path(r'^csv/upload$', views.upload_csv, name='upload_csv'),
    re_path(r'^csv/download$', views.download_csv, name='download_csv'),

    re_path(r'^(?P<pk>\d+)/unlink-image$', views.unlink_image_on_product_page, name='unlink'),
    re_path(r'^(?P<pk>\d+)/duplicate$', views.duplicate_view, name='duplicate'),
    re_path(r'^(?P<pk>\d+)/update$', views.UpdateProductView.as_view(), name='update'),
    re_path(r'^(?P<pk>\d+)/delete$', views.delete_product, name='delete'),


    re_path(r'^new$', views.CreateProductView.as_view(), name='create'),
    re_path(r'^$', views.ProductsView.as_view(), name='home'),
]

settingspatterns = [
    re_path(r'^(?P<pk>\d+)/analytics$', views.StoreSettingsView.as_view(), name='analytics'),
    re_path(r'^(?P<pk>\d+)/store$', views.StoreSettingsView.as_view(), name='store'),
    re_path(r'^(?P<pk>\d+)/general$', views.GeneralSettingsView.as_view(), name='general'),

    re_path(r'^$', views.SettingsView.as_view(), name='home'),
]





urlpatterns = [
    path('api/', include((apipatterns, app_name), namespace='api')),
    path('collections/', include((collectionpatterns, app_name), namespace='collections')),
    path('coupons/', include((couponspatterns, app_name), namespace='coupons')),
    path('images/', include((imagespatterns, app_name), namespace='images')),
    path('products/', include((productpatterns, app_name), namespace='products')),
    path('settings/', include((settingspatterns, app_name), namespace='settings')),

    re_path(r'^(?P<method>(products|carts))/(?P<pk>\d+)/delete$', views.delete_item_via_table, name='delete_item'),
    
    re_path(r'^purchase/orders/new$', views.PurchaseOrderView.as_view(), name='create_purchase_order'),

    re_path(r'^tables-actions$', views.table_actions, name='table_actions'),

    re_path(r'^orders/(?P<pk>\d+)$', views.CustomerOrderView.as_view(), name='customer_order'),
    re_path(r'^orders$', views.CustomerOrdersView.as_view(), name='customer_orders'),

    re_path(r'^customers/new$', views.CreateCustomerView.as_view(), name='create_customer'),
    re_path(r'^users/(?P<pk>\d+)$', views.UserView.as_view(), name='dashboard_user'),
    re_path(r'^users/$', views.UsersView.as_view(), name='dashboard_users'),

    re_path(r'^carts/$', views.CartsView.as_view(), name='carts'),
    re_path(r'^search/$', views.SearchView.as_view(), name='search'),
    re_path(r'^$', views.IndexView.as_view(), name='index')
]
