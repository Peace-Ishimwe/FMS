from django import template

register = template.Library()

@register.filter
def sum_values(queryset, field):
    return sum(item.get(field, 0) for item in queryset)

@register.filter
def average(queryset, field):
    count = len(queryset)
    if count == 0:
        return 0  # Return 0 to avoid division by zero
    total = sum(item.get(field, 0) for item in queryset)
    return total / count

@register.filter
def pluck(queryset, field):
    """
    Extracts a list of field values from a queryset, list of objects, or list of dicts.
    """
    result = []
    for item in queryset:
        if isinstance(item, dict):  # If item is a dictionary
            result.append(item.get(field))
        elif hasattr(item, field):  # If item is an object
            result.append(getattr(item, field, None))
            
    return result

