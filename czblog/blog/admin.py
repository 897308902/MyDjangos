# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Blogs, Bmarks, Comments, Likes


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'uname', 'marks', 'ctime','coms')
    search_fields = ('title',)


@admin.register(Bmarks)
class BmarksAdmin(admin.ModelAdmin):
    list_display = ('tags',)
    search_fields = ('tags',)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('comms', 'cblog', 'uses')
    search_fields = ('comms',)


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('like_user','like_title')
    search_fields = ('like_title',)

