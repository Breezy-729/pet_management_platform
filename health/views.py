# health/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import HealthRecord
from .forms import HealthRecordForm
from pets.models import Pet
from achievements.models import Achievement, UserAchievement


def unlock_health_record_achievement(request):
    pets = Pet.objects.filter(owner=request.user)
    records = []
    for pet in pets:
        pet_records = HealthRecord.objects.filter(pet=pet)
        records.extend(pet_records)

    if len(records) >= 1:
        achievement = get_object_or_404(Achievement, name="Experienced Pet Owner")
        user_achievement, created = UserAchievement.objects.get_or_create(
            user=request.user,
            achievement=achievement,)
        if created:
            print(f"Achievement '{achievement.name}' unlocked!")

    if len(records) >= 10:
        achievement = get_object_or_404(Achievement, name="Care Angel")
        user_achievement, created = UserAchievement.objects.get_or_create(
            user=request.user,
            achievement=achievement,)
        if created:
            print(f"Achievement '{achievement.name}' unlocked!")

    checkup_records = [r for r in records if r.record_type == "checkup"]
    if len(checkup_records) >= 5:
        achievement = get_object_or_404(Achievement, name="Health Guardian")
        user_achievement, created = UserAchievement.objects.get_or_create(
            user=request.user,
            achievement=achievement,)
        if created:
            print(f"Achievement '{achievement.name}' unlocked!")

    return

@login_required
def reminders(request):
    """show list of reminders"""
    user_pets = Pet.objects.filter(owner=request.user)
    health_records = HealthRecord.objects.filter(
        pet__in=user_pets
    ).order_by('-next_visit_date')
    return render(request, 'health/reminders.html', {'records': health_records})

@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST, user=request.user)
        if form.is_valid():
            health_record = form.save()
            messages.success(request, 'Add health record successfully.')
            unlock_health_record_achievement(request)
            return redirect('pet_profile', pet_id=health_record.pet.id)
    else:
        form = HealthRecordForm(user=request.user)
    return render(request, 'health/add_reminder.html', {'form': form})

@login_required
def edit_reminder(request, reminder_id):
    record = get_object_or_404(HealthRecord, id=reminder_id, pet__owner=request.user)
    if request.method == 'POST':
        form = HealthRecordForm(request.POST, instance=record, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update health record successfully.')
            return redirect('pet_profile', pet_id=record.pet.id)
    else:
        form = HealthRecordForm(instance=record, user=request.user)
    return render(request, 'health/edit_reminder.html', {'form': form, 'record': record})