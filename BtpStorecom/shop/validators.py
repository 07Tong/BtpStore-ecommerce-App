import datetime
import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def zip_code_validator(zip_code):
    is_match = re.match(r'\w{5}', zip_code)
    if is_match:
        return is_match.group(0)
    raise ValidationError('Zip code invalide')


def discount_pct_validator(pct):
    if pct < 0 or pct > 80:
        raise ValidationError('Reduction comprise entre 0 et 70%')
    return pct


def price_validator(price):
    if price < 0:
        raise ValidationError('Le prix ne doit pas etre inférieur à 0')
    return price


def quantity_validator(quantity):
    if quantity < 1 or quantity > 99:
        raise ValidationError("La quantité invalide valide")
    return quantity
