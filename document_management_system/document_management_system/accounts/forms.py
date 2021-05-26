from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import (
    Account,
    Employee,
    Manager
)
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm
)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Account
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('email', 'username')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('is_active',)

class EmployeeRegisterForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('username', 'email', 'password1', 'password2')

class ManagerRegisterForm(UserCreationForm):
    class Meta:
        model = Manager
        fields = ('username', 'email', 'password1', 'password2')


class PwdResetForm(PasswordResetForm):

    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = Account.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Unfortunatley we can not find that email address')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))
