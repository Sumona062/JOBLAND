from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog_title', 'date_posted',)
    search_fields = ('author',)
    readonly_fields = ('date_posted',)

    filter_horizontal = ()
    ordering = ('-date_posted',)
    fieldsets = ()
    list_filter = ('author',)


class BlogCommentModelAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog_post', 'content', 'date_posted',)
    search_fields = ('author',)
    readonly_fields = ('date_posted',)

    filter_horizontal = ()
    ordering = ('-date_posted',)
    fieldsets = ()
    list_filter = ('author',)


class BlogViewModelAdmin(admin.ModelAdmin):
    list_display = ('viewer', 'viewed', 'timestamp',)
    search_fields = ('viewer',)
    readonly_fields = ('timestamp',)

    filter_horizontal = ()
    ordering = ('-timestamp',)
    fieldsets = ()
    list_filter = ('viewer',)


class BlogSearchKeywordModelAdmin(admin.ModelAdmin):
    list_display = ('searched_by', 'searched_for', 'timestamp',)
    search_fields = ('searched_by', 'searched_for',)
    readonly_fields = ('timestamp',)

    filter_horizontal = ()
    ordering = ('-timestamp',)
    fieldsets = ()
    list_filter = ('searched_by',)


class KeywordModelAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'total_count',)
    search_fields = ('keyword',)
    readonly_fields = ()

    filter_horizontal = ()
    ordering = ('-total_count',)
    fieldsets = ()
    list_filter = ('keyword',)


admin.site.register(BlogModel, BlogModelAdmin)
admin.site.register(BlogCommentModel, BlogCommentModelAdmin)
admin.site.register(BlogViewModel, BlogViewModelAdmin)
admin.site.register(KeywordModel, KeywordModelAdmin)
admin.site.register(BlogSearchKeywordModel, BlogSearchKeywordModelAdmin)
