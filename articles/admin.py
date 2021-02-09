from django.contrib import admin
from .models import Article
from .models import Comment

# Register your models here.
class CommentInline(admin.TabularInline):
    model = Comment
    default = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)