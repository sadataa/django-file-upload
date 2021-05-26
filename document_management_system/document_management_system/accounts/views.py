from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from .forms import (
    EmployeeRegisterForm,
    ManagerRegisterForm,
    UserUpdateForm,
)
from .models import Account


def deshboard_page_view(request):
    template_name = 'account/dashboard.html'
    context = {}
    return render(request, template_name, context)

def register_all_view(request):
    template_name = 'all register.html'
    context = {}
    return render(request, template_name, context)

def all_user_view(request):
    if request.user.is_staff:
        users = Account.objects.all()
        template_name = 'account/all-user.html'
        context = {'users': users,}
        return render(request, template_name, context)
    else:
        return redirect('/')

def user_delete_view(request, pk):
    if request.user.is_staff:
        user = get_object_or_404(Account, pk=pk)
        user.delete()
        return redirect('account:all_user_view')
    else:
        return redirect('/')

def user_update_view(request, pk):
    if request.user.is_staff:
        u_user = get_object_or_404(Account, pk=pk)
        form = UserUpdateForm(request.POST or None, instance=u_user)
        if form.is_valid():
            form.save()
            return redirect('account:all_user_view')
        template_name = 'account/user-update.html'
        context = {'form': form, 'u_user': u_user,}
        return render(request, template_name, context)
    else:
        return redirect('/')


def user_login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == 'POST':
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('account:login_view')
    template_name = 'account/login.html'
    return render(request, template_name)

def employee_register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = EmployeeRegisterForm()
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('account:login_view')
    else:
        form = EmployeeRegisterForm()
    template_name = 'account/employee-register.html'
    context = {'form': form,}
    return render(request, template_name, context)

def manager_register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = ManagerRegisterForm()
    if request.method == 'POST':
        form = EmployeeRegisterForm(request.POST or None)
        if form.is_valid():
            instance = form.save()
            instance.type = Account.Types.MANAGER
            instance.is_active = False
            instance.save()
            return redirect('account:login_view')
    else:
        form = ManagerRegisterForm()
    template_name = 'account/manager-register.html'
    context = {'form': form,}
    return render(request, template_name, context)

def user_logout_view(request):
    logout(request)
    return redirect('/')

def user_profile_view(request, username):
    profile = get_object_or_404(Account, username=username)
    template_name = 'account/profile.html'
    context = {'profile': profile,}
    return render(request, template_name, context)
def user_update_view(request, pk):
    if request.user.is_staff:
        u_user = get_object_or_404(Account, pk=pk)
        form = UserUpdateForm(request.POST or None, instance=u_user)
        if form.is_valid():
            form.save()
            return redirect('account:all_user_view')
        template_name = 'account/user-update.html'
        context = {'form': form, 'u_user': u_user,}
        return render(request, template_name, context)
    else:
        return redirect('/')

def user_profile_update(request, username):
    profile = get_object_or_404(Account, username=username)
    form = UserProfileImageUpdateForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('account:profile_view', username=profile.username)
    template_name = 'account/profile-update.html'
    context = {'form': form,}
    return render(request, template_name, context)