from django import template

register=template.Library()

@register.filter
def addclass():
    return field.as_widget(attrs={'class':css})