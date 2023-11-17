from django.contrib import admin

from django.contrib.auth import get_user_model
UserModel = get_user_model()

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    model = UserModel
    list_display = 'full_name', 'email', 'business_category', 'is_active', 'is_superuser', 'date_joined'
    list_editable = 'business_category',
    list_display_links = 'full_name', 'email'