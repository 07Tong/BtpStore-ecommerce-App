from django import forms
from django.forms import widgets
from django.forms import fields
from shop import validators

class CouponForm(forms.Form):
    coupon = fields.CharField(max_length=5, widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coupon'}))

    def clean(self):
        coupon = self.cleaned_data['coupon']
        if coupon == 'AWST':
            raise forms.ValidationError("Code invalide")
        return self.cleaned_data

class ShipmentForm(forms.Form):
    first_name = forms.CharField(widget=widgets.TextInput(attrs={'name': 'firstname'}))
    last_name   = forms.CharField(widget=widgets.TextInput(attrs={'name': 'lastname'}))
    
    email   = forms.EmailField(widget=widgets.EmailInput())

    telephone = forms.CharField(widget=widgets.TextInput())

    address   = forms.CharField()
    COUNTRIES = [('cameroun', 'Cameroun'), ('tchad', 'Tchad')]
    country     = forms.CharField(widget=widgets.Select(choices=COUNTRIES))
    CITIES = [
        ('yaoundé', 'Yaoundé'),
        ('douala', 'Douala'),
        ('ebolowaca', 'Ebolowa'),
        ('bertoua', 'Bertoua'),
    ]
    city        = forms.CharField(widget=widgets.Select(choices=CITIES))
    zip_code    = forms.CharField(validators=[validators.zip_code_validator])

    billing_equals_shipping = forms.BooleanField(required=False, initial=False)
    save_for_next_time      = forms.BooleanField(required=False, initial=False)

    def clean(self):
        cleaned_data = super().cleaned_data
        return cleaned_data
