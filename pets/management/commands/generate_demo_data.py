from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import random
from faker import Faker
from pets.models import Pet
from health.models import HealthRecord
from achievements.models import Achievement, UserAchievement
from users.models import UserProfile

class Command(BaseCommand):
    help = 'Generate demo data'

    def handle(self, *args, **kwargs):
        fake = Faker(['en_US'])
        
        # 1. Create 3 fixed users and profiles
        self.stdout.write('Creating users and profiles...')
        users = []
        predefined_users = [
            {'username': 'jack', 'first_name': 'Jack', 'last_name': 'Smith'},
            {'username': 'rose', 'first_name': 'Rose', 'last_name': 'Williams'},
            {'username': 'mike', 'first_name': 'Mike', 'last_name': 'Johnson'}
        ]

        for user_data in predefined_users:
            if not User.objects.filter(username=user_data['username']).exists():
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=f"{user_data['username']}@example.com",
                    password='123456',
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name']
                )
                UserProfile.objects.create(
                    user=user,
                    timezone='UTC',
                    notification_preference=random.choice(['email', 'app'])
                )
                users.append(user)
            else:
                users.append(User.objects.get(username=user_data['username']))

        # 2. Create 10 pets
        self.stdout.write('Creating pets...')
        pets = []
        dog_breeds = ['Golden Retriever', 'Labrador', 'Husky', 'Corgi', 'Border Collie']
        cat_breeds = ['Persian', 'Siamese', 'Maine Coon', 'British Shorthair', 'Ragdoll']
        rabbit_breeds = ['Holland Lop', 'Dutch Rabbit', 'Angora', 'Rex Rabbit']
        hamster_breeds = ['Syrian', 'Dwarf Campbell', 'Winter White', 'Roborovski']

        pet_names = [
            'Luna', 'Bella', 'Charlie', 'Lucy', 'Leo',
            'Max', 'Milo', 'Oliver', 'Rocky', 'Daisy'
        ]
        pet_species = [
            'dog', 'dog', 'dog', 'dog', 'dog', 
            'cat', 'cat', 'cat', 'rabbit', 'hamster',
        ]

        # Create exactly 10 pets
        for i in range(10):
            species = pet_species[i]
            if species == 'dog':
                breed = random.choice(dog_breeds)
            elif species == 'cat':
                breed = random.choice(cat_breeds)
            elif species == 'rabbit':
                breed = random.choice(rabbit_breeds)
            else:
                breed = random.choice(hamster_breeds)

            pet = Pet.objects.create(
                owner=random.choice(users),  # Randomly assign to one of the three users
                name=pet_names[i],
                species=species,
                breed=breed,
                photo=f'pets/{i+1}.jpg',
                birthdate=fake.date_between(start_date='-5y', end_date='-1m'),
                gender=random.choice(['M', 'F', 'U']),
                weight=round(random.uniform(0.5, 30), 2),
                description=fake.text(max_nb_chars=200)
            )
            pets.append(pet)

        # 3. Create exactly 10 health records
        self.stdout.write('Creating health records...')
        symptoms_by_status = {
            'sick': ['Loss of appetite', 'Lethargy', 'Fever', 'Coughing', 'Digestive issues'],
            'recovering': ['Improving appetite', 'Increased energy', 'Mild symptoms'],
            'critical': ['Severe dehydration', 'Acute pain', 'Breathing difficulty']
        }

        treatments = [
            'Prescribed antibiotics',
            'Recommended rest and monitoring',
            'Administered vaccines',
            'Dietary modification',
            'Prescribed pain medication'
        ]

        clinic_names = [
            'Pawsome Pet Clinic',
            'Happy Tails Veterinary',
            'Animal Care Center',
            'Pet Health Hospital',
            'Companion Care Clinic'
        ]

        # Create exactly 10 health records
        for i in range(10):
            record_date = fake.date_between(
                start_date='-1y',
                end_date='today'
            )
            status = random.choice(['healthy', 'sick', 'recovering', 'critical'])
            
            HealthRecord.objects.create(
                pet=random.choice(pets),  # Randomly assign to one of the pets
                record_type=random.choice(['vaccine', 'checkup', 'treatment', 'routine']),
                record_date=record_date,
                status=status,
                weight=round(random.uniform(0.5, 30), 2),
                temperature=round(random.uniform(37.5, 39.5), 1),
                symptoms=random.choice(symptoms_by_status.get(status, [''])) if status != 'healthy' else '',
                diagnosis=fake.sentence() if status != 'healthy' else '',
                treatment=random.choice(treatments) if status != 'healthy' else '',
                next_visit_date=record_date + timedelta(days=random.randint(7, 30)) if status != 'healthy' else None,
                vet_name=fake.name(),
                clinic_name=random.choice(clinic_names),
                notes=fake.sentence() if random.random() > 0.5 else ''
            )

        # 4. Create exactly 10 achievements
        self.stdout.write('Creating achievements...')
        achievement_data = [
            ('Novice Pet Owner', 'Adopt your first pet', 'Adopt one pet', 3, 'beginner'),
            ('Information craftsman', 'Complete your account profile', 'Complete your account profile', 3, 'beginner'),
            ('Experienced Pet Owner', 'Create first health record', 'Create first health record', 3, 'intermediate'),
            ('Health Guardian', 'Complete five checkups', 'Pet checkup 5 times', 4, 'health'),
            ('Care Angel', 'Record 10 health statuses', 'Record pet health status 10 times', 5, 'care'),
            ('Perfect Pet Parent', 'Adopt three pets', 'Adopt three pets', 5, 'master'),
        ]

        achievements = []
        for name, desc, req, points, category in achievement_data:
            achievement = Achievement.objects.create(
                name=name,
                description=desc,
                requirement=req,
                points=points,
                category=category,
            )
            achievements.append(achievement)

        self.stdout.write(self.style.SUCCESS('Successfully generated demo data!'))