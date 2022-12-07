from django.contrib import admin
from django.utils.safestring import mark_safe

from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cat', 'get_html_image', 'time_create', 'is_published']
    list_display_links = ['id', 'title'] #можно переходить в редактирование нажимая на эти поля
    search_fields = ['id', 'title']
    list_editable = ['is_published', 'cat'] #можно менять не входя в каждую запись
    list_filter = ['is_published', 'time_create']
    # filter_horizontal = ['cat']
    prepopulated_fields = {'slug': ('title',)} #автоматическое заполнение на основе title
    fields = ['title', 'slug', 'source', 'cat', 'content', 'image', 'get_html_image', 'is_published', 'time_create', 'time_update'] #порядок отображения при редактировании
    readonly_fields = ['time_create', 'time_update', 'get_html_image']

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_image.short_description = 'Миниатюра'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


