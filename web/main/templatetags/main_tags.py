from django import template
from ..models import *


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('main/show_categories.html')
def show_categories(cat_selected):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}
