from django.contrib import admin
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display = ('user', 'phone_number', 'website', 'picture')
    list_display_links = ('user', 'website')
    list_editable = ('phone_number', 'picture')
    search_fields = ('user__email', 'user__first_name', 'user_last_name')
    list_filter = ('created', 'modified')