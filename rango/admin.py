from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page





class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  # 自定义页面列表显示的字段


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
# Update the registration to include this customised interface



admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)