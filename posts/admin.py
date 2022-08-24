from django.contrib import admin

from posts.models import Posts, Tag


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "slug", "created_at")
    fields = ("author", "title", "slug", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")
    raw_id_fields = ("author",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # list_display = ("title")
    # fields = ("title")
    # readonly_fields = ("title")
    search_fields = (["title"])
    # raw_id_fields = ("title")