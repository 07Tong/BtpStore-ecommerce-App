from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import fields, signals
from django.dispatch import receiver

MYUSER = get_user_model()

class DashboardSetting(models.Model):
    myuser    = models.OneToOneField(MYUSER, on_delete=models.CASCADE)
    dark_mode = fields.BooleanField(default=False)

    name = models.CharField(max_length=50)

    contact_email = models.EmailField(max_length=100)
    customer_care_email = models.EmailField(max_length=100)
 
    legal_name = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=10, blank=True, null=True)
     
    class StoreCurrencies(models.Choices):
        FCFA = 'fcfa'
        #DOLLARS = 'dollars'
    store_currency = models.CharField(
        max_length=10, choices=StoreCurrencies.choices, default=StoreCurrencies.FCFA)
    tax_rate = models.IntegerField(default=20)

    
    automatic_archive = models.BooleanField(
        default=False, help_text='Archive an order automatically after it has been fulfilled and paid')

    
    allow_coupons = models.BooleanField(default=False)
    allow_accounts = models.BooleanField(default=False)
     
    objects = models.Manager()

    def __str__(self):
        return self.myuser.email

@receiver(signals.post_save, sender=MYUSER)
def create_user_dashboard(instance, sender, created, **kwargs):
    if created:
        DashboardSetting.objects.create(myuser=instance)
