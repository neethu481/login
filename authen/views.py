from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return render(request, 'authen/dashboard.html',{})
            return get_users_view(request)
    else:
        form = UserCreationForm()
    return render(request, 'authen/signup.html', {'form': form})


def landing_view(request):
    return render(request, 'authen/landing.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return render(request, 'authen/dashboard.html',{})
            return get_users_view(request)
    else:
        form = AuthenticationForm()
    return render(request, 'authen/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/landing')


def get_users_view(request):
    all_users = get_user_model().objects.all()
    context = {'all_users': all_users}
    return render(request, 'authen/dashboard.html', context)


def dropdown_view(request):
    if request.method == 'POST':
        username = request.POST['item_id']
        print(username)
        u = get_user_model().objects.get(username=username)
        u.delete()
        return get_users_view(request)