from django import template

register = template.Library()

@register.filter
def add_class(field, class_name):
    """Add a class to a form field widget."""
    return field.as_widget(attrs={'class': class_name})