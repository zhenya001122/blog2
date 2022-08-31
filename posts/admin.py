from django.contrib import admin

from posts.models import Post, Tag, Address


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "slug", "created_at")
    fields = ("author", "title", "slug", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "slug", "text")
    raw_id_fields = ("author",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fields = ("title", 'posts')
    readonly_fields = ("title",)
    search_fields = ["title"]
    # raw_id_fields = ("title",)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("author", "city", "street", "house_number", "phone", "email")
    fields = ("author", "city", "street", "house_number", "phone", "email")
    search_fields = ("author",)