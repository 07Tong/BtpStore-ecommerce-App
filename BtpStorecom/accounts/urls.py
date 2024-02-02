from django.contrib import admin
from django.urls import include, path ,re_path
from django.views.generic import TemplateView

from accounts import views, views_profile

app_name = 'accounts'

profile_patterns = [
    re_path(r'^profile/payment-methods/$', views_profile.PaymentMethodsView.as_view(), name='payment_methods'),
    re_path(r'^profile/delete/$', views_profile.ProfileDeleteView.as_view(), name='delete_account'),
    re_path(r'^profile/data/$', views_profile.ProfileDataView.as_view(), name='profile_data'),
    re_path(r'^profile/change-password/$', views_profile.ChangePasswordView.as_view(), name='change_password'),
    re_path(r'^profile/$', views_profile.ProfileView.as_view(), name='profile'),
]

urlpatterns = [
    path('profile/', include(profile_patterns)),

    re_path(r'^forgot-password/confirm/(?P<uidb64>[A-Z]+)/(?P<token>\w+\-\w+)$',
            views.UnauthenticatedPasswordResetView.as_view(), name='password_reset_confirm'),
    re_path(r'^forgot-password/$', views.ForgotPasswordView.as_view(), name='forgot_password'),
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    re_path(r'^signup/$', views.SignupView.as_view(), name='signup'),
    
]
