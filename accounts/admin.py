from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CreateCustomUserForm, ChangeCustomUserForm

# Register your models here.
CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CreateCustomUserForm
    form = ChangeCustomUserForm
    model = CustomUser
    list_display = [
        "username",
        "email",
        "is_staff",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
