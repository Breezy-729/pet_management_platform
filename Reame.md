### Running Method:

**Step 0:** Delete the `db.sqlite3` database file first.

**Step 1:** Generate database tables using the following commands:
```sh
python manage.py makemigrations
python manage.py migrate
```

**Step 2:** Create demo data:
```sh
python manage.py generate_demo_data
```

**Step 3:** Start the server:
```sh
python manage.py runserver
```

**SQLiteExpertPro** can be used to view the SQLite database.

---

### List of Required HTML Files for the Pet Management Platform:

#### **Global Templates**
1. `templates/base.html` - Base template, inherited by all pages.
2. `templates/home.html` - Homepage (should not inherit from the base template).

#### **User Authentication & Profile Pages**
3. `templates/users/login.html` - User login page.
4. `templates/users/register.html` - New user registration page.
5. `templates/users/profile.html` - User profile page.
6. `templates/users/logout.html` - Logout confirmation page.

#### **Pet Management Pages**
7. `templates/pets/pet_management.html` - Overview page for managing pets (displays all pets owned by the user).
8. `templates/pets/pet_profile.html` - Detailed pet profile page.
9. `templates/pets/add_pet.html` - Form page for adding a new pet.
10. `templates/pets/edit_pet.html` - Page for editing pet information.
11. `templates/pets/delete_pet.html` - Confirmation page for deleting a pet.

#### **Health Reminder Pages**
12. `templates/health/reminders.html` - Health reminders list page.
13. `templates/health/add_reminder.html` - Form page for adding a new reminder.
14. `templates/health/edit_reminder.html` - Page for editing reminder details.

#### **Achievement System Pages**
15. `templates/achievements/achievements.html` - Page for displaying achievements and badges.

---

### **Project Directory Structure**

```
pet_management_platform/            # Project root directory
│
├── pet_management/                 # Main application
│   ├── __init__.py
│   ├── settings.py                 # Project settings
│   ├── urls.py                      # Main URL routing (includes URLs of all apps)
│   ├── wsgi.py                      # WSGI configuration
│   ├── asgi.py                      # ASGI configuration
│   └── views.py                      # Main application views
│
├── static/                          # Static files
│   ├── css/
│   │   ├── bootstrap.min.css        # Bootstrap framework
│   │   └── style.css                # Custom CSS
│   ├── js/
│   │   ├── jquery.min.js            # jQuery library
│   │   ├── bootstrap.min.js         # Bootstrap JS
│   │   └── app.js                   # Custom JavaScript
│   └── images/                      # Image assets
│
├── templates/                       # Global templates
│   ├── base.html                     # Base template (inherited by all pages except the homepage)
│   └── home.html                     # Independent homepage template (does not inherit from base.html)
│
├── users/                            # User app
│   ├── __init__.py
│   ├── models.py                     # User models
│   ├── views.py                       # View functions (including form definitions)
│   └── templates/                     # App-specific templates
│       └── users/
│           ├── login.html             # Login page
│           ├── register.html          # Registration page
│           ├── profile.html           # User profile page
│           └── logout.html            # Logout page
│
├── pets/                              # Pet management app
│   ├── __init__.py
│   ├── models.py                     # Pet models
│   ├── views.py                       # View functions (including form definitions)
│   └── templates/                     # App-specific templates
│       └── pets/
│           ├── pet_profile.html       # Pet profile page
│           ├── pet_management.html    # Pet management page
│           ├── add_pet.html           # Add pet page
│           └── edit_pet.html          # Edit pet page
│
├── health/                            # Health record app
│   ├── __init__.py
│   ├── models.py                     # Health record models
│   ├── views.py                       # View functions (including form definitions)
│   └── templates/                     # App-specific templates
│       └── health/
│           ├── reminders.html         # Health reminders page
│           └── add_reminder.html      # Add reminder page
│
├── achievements/                      # Achievements app
│   ├── __init__.py
│   ├── models.py                     # Achievement models
│   ├── views.py                       # View functions
│   └── templates/                     # App-specific templates
│       └── achievements/
│           └── achievements.html      # Achievements page
│
└── manage.py                          # Django management script
```