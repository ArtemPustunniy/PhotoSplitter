from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from support.models import User
from support.views import menu


def register(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():
                try:
                    User.objects.get(email=user_form.cleaned_data['email'])
                except:
                    new_user = user_form.save(commit=False)
                    new_user.set_password(user_form.cleaned_data['password'])
                    new_user.save()
                    return redirect('login')
            return redirect('reg')

        else:
            user_form = UserRegistrationForm()
        return render(request, 'support/reg.html', {'user_form': user_form, 'menu': menu})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            error_message = 'Пользователь не найден'
            return render(request, 'support/login.html', {'error_message': error_message})
    else:
        return render(request, template_name='support/login.html')


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    logout(request)
    return redirect('main')