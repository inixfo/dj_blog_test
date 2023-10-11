from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app_login.forms import SignUpForm, UserProfileChange

# Create your views here.
def signup(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form': form, 'registered':registered}
    return render(request, 'app_login/signup.html', context=dict)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    return render (request, 'app_login/login.html', context={'form': form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



@login_required
def profile(request):
    return render(request, 'App_Login/profile.html', context={})


@login_required
def user_change(request):
    current_user = request.user
    changed = False
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            changed = True
    return render(request, 'app_login/change_profile.html', context={'form':form, 'changed': changed})


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render (request, 'app_login/change_pass.html', context={'form':form, 'changed':changed})
