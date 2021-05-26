from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
    Account,
    Employee,
    EmployeeMore,
    Manager,
    ManagerMore,
)


@admin.register(Account)
class AccountAdminModel(UserAdmin):
    list_display = ('username', 'email', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser')
    readonly_fields = ('id', 'date_joined', 'last_login')
    list_filter = ('last_login', 'username', 'email')
    search_fields = ('username', 'email')
    filter_horizontal = ()
    fieldsets = ()
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'type', 'password1', 'password2')}
        ),
    )
class EmployeeMoreInline(admin.TabularInline):
    model = EmployeeMore

@admin.register(Employee)
class EmployeeAdminModel(admin.ModelAdmin):
    inlines = [EmployeeMoreInline]

class ManagerMoreInline(admin.TabularInline):
    model = ManagerMore

@admin.register(Manager)
class MonagerAdminModel(admin.ModelAdmin):
    inlines = [ManagerMoreInline]
