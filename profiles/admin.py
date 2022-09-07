from django.contrib import admin

from profiles.models import AddressDelivery


@admin.register(AddressDelivery)
class AddressDeliveryAdmin(admin.ModelAdmin):
    list_display = ("author", "city", "street", "house_number", "phone",)
    fields = ("author", "city", "street", "house_number", "phone",)
    search_fields = ("author",)
