from django import template
from blog.models import *


register = template.Library()


#простой пользовательский тег, чтобы не передавать несколько раз в разных views
@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


#включающий пользовательский тег, возвращает сразу html страницу
@register.inclusion_tag('blog/list_categories.html')
def show_categories(sort=None, cat_selected=0): #параметры передаются в template
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.simple_tag()
def get_menu():
    menu = [{'title': 'О сайте', 'url_name': 'about'},
            {'title': 'Добавить статью', 'url_name': 'add_page'},
            {'title': 'Обратная связь', 'url_name': 'contact'},
            {'title': 'Войти', 'url_name': 'login'},
            ]
    return menu