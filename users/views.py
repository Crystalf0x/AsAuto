from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from users.forms import LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.forms import RegisterForm


# Create your views here.
def handle_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('parts:parts'))
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {
        'form': form
    })


def handle_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def register(request):
    form = RegisterForm()
    return render(request, 'users/register.html', {
        'form': form
    })