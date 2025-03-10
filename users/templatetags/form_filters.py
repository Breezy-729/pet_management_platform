from django import template
from django.utils import timezone

register = template.Library()

@register.filter(name='addclass')
def addclass(field, css_class):
    """Add CSS class for form fields"""
    return field.as_widget(attrs={"class": css_class})

@register.filter
def is_future_date(date):
    if date is None:
        return False
    return date >= timezone.now().date()