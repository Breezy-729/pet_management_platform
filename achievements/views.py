# achievements/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Achievement, UserAchievement

@login_required
def achievements(request):
    """view of achievements list"""
    all_achievements = Achievement.objects.all()
    user_achievements = UserAchievement.objects.filter(
        user=request.user
    ).select_related('achievement')
    
    achievements_data = []
    for achievement in all_achievements:
        is_completed = user_achievements.filter(achievement=achievement).first() is not None
        print('completed:', is_completed)
        achievements_data.append({
            'achievement': achievement,
            'is_completed': is_completed
        })

    context = {
        'achievements_data': achievements_data,
        'completed_count': user_achievements.count()
    }
    return render(request, 'achievements/achievements.html', context)