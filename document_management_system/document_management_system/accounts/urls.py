from django.urls import path,include
from django.contrib.auth import views as auth_views
from .forms import PwdResetConfirmForm, PwdResetForm
from django.views.generic import TemplateView
from .views import (
    deshboard_page_view,
    employee_register_view,
    manager_register_view,
    user_login_view,
    user_logout_view,
    all_user_view,
    register_all_view,
    user_update_view,
    user_delete_view,
    user_profile_update,
    user_profile_view,
)

app_name = 'accounts'
urlpatterns = [
    path('dashboard/', deshboard_page_view, name='dashboard_view'),
    path('register-all_view/', register_all_view, name='register_all_view'),
    path('register/', employee_register_view, name='register_view'),
    path('manager-register/', manager_register_view, name='manager_register_view'),
    path('login/', user_login_view, name='login_view'),
    path('logout/', user_logout_view, name='logout_view'),
    path('all-user/', all_user_view, name='all_user_view'),
    path('user-update/<int:pk>/', user_update_view, name='user_update_view'),
    path('user-delete/<int:pk>/', user_delete_view, name='user_delete'),
    path('user-update/<int:pk>/', user_update_view, name='user_update_view'),
    path('user-delete/<int:pk>/', user_delete_view, name='user_delete'),


    # password reset
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset/password_reset_form.html",
            success_url="password_reset_email_confirm",
            email_template_name="account/password_reset/password_reset_email.html",
            form_class=PwdResetForm,
        ),
        name="pwdreset",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset/password_reset_confirm.html",
            success_url="password_reset_complete/",
            form_class=PwdResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/password_reset_email_confirm/",
        TemplateView.as_view(template_name="account/password_reset/reset_status.html"),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/Mg/password_reset_complete/",
        TemplateView.as_view(template_name="account/password_reset/reset_status.html"),
        name="password_reset_complete",
    ),
]