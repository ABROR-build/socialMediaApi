from django.contrib import admin
from . import models


# class PostsAdmin(admin.ModelAdmin):
#     list_display = ['user', 'caption', 'image']
#
#
# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ['commenter', 'post', 'comment']
#
#
# class PostLikesAdmin(admin.ModelAdmin):
#     list_display = ['user', 'post', 'like']
#
#
# class CommentLikesAdmin(admin.ModelAdmin):
#     list_display = ['user', 'comment', 'like']


admin.site.register(models.Posts)
admin.site.register(models.Comments)
admin.site.register(models.PostLikes)
admin.site.register(models.CommentLikes)
