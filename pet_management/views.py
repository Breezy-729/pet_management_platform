# pet_management/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Home page view.
    If user is authenticated, redirect to dashboard.
    """
    return render(request, 'home.html')

@login_required
def dashboard(request):
    """
    Main dashboard view for authenticated users.
    Shows overview of pets, recent activities, and achievements.
    """
    context = {
        'total_pets': request.user.pets.count(),
        'total_achievements': request.user.achievements.filter(is_completed=True).count(),
        'recent_records': request.user.pets.select_related('health_records').order_by('-created_at')[:5]
    }
    return render(request, 'dashboard.html', context)