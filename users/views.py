# users/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile
from achievements.models import Achievement, UserAchievement


def unlock_profile_achievement(request):
    print('enter unlock')
    curr_user = request.user
    user_info_completed = curr_user.email and curr_user.first_name and curr_user.last_name
    profile_completed = curr_user.profile.avatar and curr_user.profile.timezone
    print('enter unlock1')
    if user_info_completed and profile_completed:
        print('enter unlock comnpleted')
        achievement = get_object_or_404(Achievement, name="Information craftsman")
        if not achievement:
            print('No Information craftsman achievement.')
            return

        user_achievement, created = UserAchievement.objects.get_or_create(
            user=request.user,
            achievement=achievement)

        if created:
            print(f'Achievement {achievement.name} is created')
    return


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, 'Account successfully created! Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the errors in the form.') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
    
def login_view(request): 
    if request.method == 'POST': 
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(username=username, password=password) 
        if user is not None: 
            login(request, user) 
            messages.success(request, 'Login successful!') 
            return redirect('home') 
        else: 
            messages.error(request, 'Incorrect username or password.') 
    return render(request, 'users/login.html')

@login_required
def profile(request):
    """user profile view"""
    if request.method == 'POST':
        print('POST req')
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profie updated successfully.')
            unlock_profile_achievement(request)
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out!')
    return redirect('home')

def home(request):
    return render(request, 'home.html')