from django.contrib import admin

from userauths.models import User, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'phone', 'is_staff')
    search_fields = ('username', 'email')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'verified')
    search_fields = ('user__username', 'full_name')


admin.site.register(User, UserAdmin)
admin.site.register(Profile, UserProfileAdmin)
