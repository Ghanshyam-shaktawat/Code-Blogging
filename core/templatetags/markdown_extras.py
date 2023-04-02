from django import template
from django.template.defaultfilters import stringfilter

import markdown2 as markdown

register = template.Library()


@register.filter()
@stringfilter
def convert_to_markdown(value):
    return markdown.markdown(value)