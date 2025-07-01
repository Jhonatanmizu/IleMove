from django.contrib import admin

from .models import Address, CustomUser


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "state", "country", "zip_code")


class AddressInline(admin.StackedInline):
    model = Address
    extra = 1


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name")
    inlines = (AddressInline,)
