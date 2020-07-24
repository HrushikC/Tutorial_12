from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    data = context['request'].GET.copy()
    for key, value in kwargs.items():
        data[key] = value
    for key in [key for key, value in data.items() if not value]:
        del data[key]
    return data.urlencode()