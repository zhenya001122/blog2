from django.contrib import admin

from posts.models import Addres


@admin.register(Addres)
class AddresAdmin(admin.ModelAdmin):
    list_display = ("author", "city", "street", "house_number", "phone",)
    fields = ("author", "city", "street", "house_number", "phone",)
    search_fields = ("author",)
