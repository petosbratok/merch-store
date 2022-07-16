from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)

@register.filter(name='substract')
def subtract(value, arg):
    return value - arg

@register.filter(name='create_delay')
def create_delay(value, arg):
    return value * arg
