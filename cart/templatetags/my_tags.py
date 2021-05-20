from decimal import *
from django import template

register = template.Library()


@register.simple_tag()
def multiple(number, value):
    return round(number * Decimal(value), 3)
    # return 344
