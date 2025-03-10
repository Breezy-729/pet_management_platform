# pets/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pet
from achievements.models import Achievement, UserAchievement
from .forms import PetForm


# unlock pet achievements
def unlock_pet_achivement(request):
    user_achievements = UserAchievement.objects.filter(
        user=request.user
    ).select_related('achievement')

    pets = Pet.objects.filter(owner=request.user)

    # unlock Novice Pet Owner
    if len(pets) >= 1:
        achievement = get_object_or_404(Achievement, name="Novice Pet Owner")
        user_achievement, created = UserAchievement.objects.get_or_create(
            user=request.user,
            achievement=achievement,)

        if created:
            print(f"Achievement '{achievement.name}' unlocked!")

    # unlock Perfect Pet Owner
    if len(pets) >= 3:
        achievement = get_object_or_404(Achievement, name="Perfect Pet Parent")
        user_achievement, created = UserAchievement.objects.get_or_create(
            user=request.user,
            achievement=achievement,)

        if created:
            print(f"Achievement '{achievement.name}' unlocked!")

    return


@login_required
def pet_management(request):
    pets = Pet.objects.filter(owner=request.user)
    return render(request, 'pets/pet_management.html', {'pets': pets})

@login_required
def pet_profile(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
    health_records = pet.health_records.all().order_by('-record_date')
    context = {
        'pet': pet,
        'health_records': health_records
    }
    return render(request, 'pets/pet_profile.html', context)

@login_required
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            messages.success(request, 'Add pet successfully.')
            unlock_pet_achivement(request)
            return redirect('pet_management')
    else:
        form = PetForm()
    return render(request, 'pets/add_pet.html', {'form': form})

@login_required
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update pet profile successfully.')
            return redirect('pet_profile', pet_id=pet.id)
    else:
        form = PetForm(instance=pet)
    return render(request, 'pets/edit_pet.html', {'form': form, 'pet': pet})

@login_required
def delete_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
    if request.method == 'POST':
        pet.delete()
        messages.success(request, 'Pet profile deleted.')
        return redirect('pet_management')
    return render(request, 'pets/delete_pet.html', {'pet': pet})