from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from .forms import AccountChangeForm, AccountCreationForm


class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2'), }),
    )
    list_display = (
        'id', 'username', 'first_name', 'last_name', 'image_tag', 'is_superuser', 'is_active', 'is_staff', 'date_modified',
        'date_created')
    ordering = None
    readonly_fields = ('date_modified', 'date_created')
    list_filter = ('date_created', 'is_superuser', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'image', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff',
                                    'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('date_modified', 'date_created')}),
    )

    search_fields = ('username', 'first_name', 'last_name')


admin.site.register(Account, AccountAdmin)
