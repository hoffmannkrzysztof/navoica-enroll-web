from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from navoica_enroll.users.forms import UserChangeForm, UserCreationForm
from navoica_enroll.users.models import UserRegistrationCourse

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User",
                  {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(UserRegistrationCourse)
class UserRegistrationCourseAdmin(admin.ModelAdmin):
    pass
