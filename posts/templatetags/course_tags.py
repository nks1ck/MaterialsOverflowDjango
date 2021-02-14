from django import template
from posts.models import Category, Course

register = template.Library()

@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('courses/last_courses.html')
def get_last_courses():
    courses = Course.objects.order_by('id')[:5]
    return {'last_courses': courses}