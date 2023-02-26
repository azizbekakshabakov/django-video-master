from django.contrib import admin

from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'first_name', 'last_name', 'icon')
    list_display_links = ('id', 'login')
    search_fields = ('login', 'first_name', 'last_name')
    list_editable = ('first_name', 'last_name')
    list_filter = ('first_name',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'index', 'video', 'preview', 'user_id')
    list_display_links = ('id', 'index')
    search_fields = ('index',)
    list_editable = ('user_id',)
    list_filter = ('index',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'user_id', 'video_id')
    list_display_links = ('id',)
    search_fields = ('content', 'video_id')
    list_editable = ('content',)
    list_filter = ('content', 'video_id')

class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user_id')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_editable = ('name',)
    list_filter = ('name', 'user_id')

class PlaylistContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'playlist_id')
    list_display_links = ('id',)
    search_fields = ('playlist_id',)
    list_editable = ('url',)
    list_filter = ('playlist_id',)

admin.site.register(User, UserAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(PlaylistContent, PlaylistContentAdmin)