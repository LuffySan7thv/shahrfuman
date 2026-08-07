from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, 'رمز عبور و تکرار آن مطابقت ندارند')
            return render(request, 'accounts/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً ثبت شده است')
            return render(request, 'accounts/register.html')

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, 'ثبت‌نام با موفقیت انجام شد')
        return redirect('core:home')

    return render(request, 'accounts/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'خوش آمدید')
            return redirect('core:home')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    messages.info(request, 'با موفقیت خارج شدید')
    return redirect('core:home')


