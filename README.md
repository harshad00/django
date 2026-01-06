# Django Project Creation Guide (Windows)

This document explains how to create a Django project step by step on a Windows system.  
It also includes solutions for the common error:  
**`'django-admin' is not recognized as an internal or external command`**

---

## 1. Check Python Installation

Open **Command Prompt (CMD)** and run:

```bash
python --version
```

## 2. Install Django

```
python -m pip install django
```

## 3. Create Django Project

```
python -m django startproject myproject
```

## 4. Project Structure

```
myproject/
 ├── manage.py
 └── myproject/
     ├── __init__.py
     ├── settings.py
     ├── urls.py
     ├── asgi.py
     └── wsgi.py
```

## 5. Run Django Development Server

```
cd myproject

## Start the server: ##
python manage.py runserver 

## Open the browser and visit: ##
http://127.0.0.1:8000/

```

## What does -m mean in Python?

- m means:

   Run a library/module as a program

   “Find the django module and run it using this Python.”


# Django URL & View Setup (Project + App)

This document explains how to:
- Create views
- Add app-level URLs
- Connect app URLs to project URLs
- Display pages in the browser

---

## 1. Django URL Flow (Very Important)

Request flow in Django:

Browser  
→ `project/urls.py`  
→ `app/urls.py`  
→ `views.py`  
→ Response (HTML / Text)

---

## 2. Create a Django App

Run this command inside your project folder (where `manage.py` exists):

```bash
python manage.py startapp mycrudapp
```

## 3. Register App in Settings
Open:
```
myproject/settings.py
```
Add your app inside INSTALLED_APPS:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mycrudapp',   # ← added app
]
```

## 4. Create a View (Page Logic)

```
mycrudapp/views.py
```
Add this code:
```
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Home Page")

def about(request):
    return HttpResponse("About Page")

def contact(request):
    return HttpResponse("Contact Page")

```

## 5. Create App-Level URLs

Create a new file:

```
mycrudapp/urls.py
```
Add this code:
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
```
## 6. Connect App URLs to Project URLs

Open:
```
myproject/urls.py
```
Update it like this:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
]
```
## 7. Run the Server
```
python manage.py runserver
```

---


# Django Templates Setup Guide

This document explains how to configure and use **HTML templates** in a Django project.


---


## 1. Recommended Folder Structure

Create a `templates` folder at the **project root level** (same level as `manage.py`).
```
crud/folder
├── manage.py
├── crud/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── mycrudapp/
│ ├── views.py
│ ├── urls.py
│ └── ...
└── templates/
└── mycrudapp/
├── base.html
├── home.html
└── about.html
```

---

## 2. Configure Templates in settings.py

Open `crud/settings.py` and update the `TEMPLATES` section:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ], # 👈 IMPORTANT
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

## 3. Create Views to Render Templates

Open mycrudapp/views.py:
```
from django.shortcuts import render

def home(request):
    return render(request, 'mycrudapp/home.html')

def about(request):
    return render(request, 'mycrudapp/about.html')
```

## 4.Create App-Level URLs

Create or update mycrudapp/urls.py:
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]

```

## 5. Connect App URLs to Project URLs

Open crud/urls.py:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mycrudapp.urls')),
]

```

## 6. Create HTML Template Files
templates/mycrudapp/home.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to CRUD Home Page</h1>
    <a href="/about/">About</a>
</body>
</html>

```

about.html
```html
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
</head>
<body>
    <h1>About Page</h1>
    <a href="/">Home</a>
</body>
</html>

```

## 7. Run the Development Server

```bash
python manage.py runserver

outpu: 
http://127.0.0.1:8000/
http://127.0.0.1:8000/about/
```

# Django Static Files Setup (CSS)

This document explains how to configure **static files** (CSS) in a Django project and use them inside HTML templates.

---

## 1. Recommended Folder Structure

Create a `static` folder at the **project root level** (same level as `manage.py`).
```
crud/
├── manage.py
├── crud/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── mycrudapp/
│ ├── views.py
│ ├── urls.py
│ └── ...
├── templates/
│ └── mycrudapp/
│ ├── home.html
│ └── about.html
└── static/
└── mycrudapp/
└── css/
└── style.css
```

📌 Best practice:  
`static/app_name/css/style.css`

---

## 2. Configure Static Files in settings.py

Open `crud/settings.py` and add/update the following:

```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```
⚠️ Do NOT remove STATIC_URL.

## 3. Create CSS File

Create the file:
```
static/mycrudapp/css/style.css
```
Add sample CSS:
```css
body {
    background-color: #f4f6f8;
    font-family: Arial, sans-serif;
}

h1 {
    color: #2c3e50;
}

a {
    color: #007bff;
    text-decoration: none;
}
```
## 4. Load Static Files in HTML Template

Open your HTML file:
```
templates/mycrudapp/home.html
```
At the top of the file, load static:
```
{% load static %}
```

Link the CSS file:
```
<link rel="stylesheet" href="{% static 'mycrudapp/css/style.css' %}">
```

## 5. Complete home.html Example
``` html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <link rel="stylesheet" href="{% static 'mycrudapp/css/style.css' %}">
</head>
<body>
    <h1>Welcome to CRUD Home Page</h1>
    <a href="/about/">About</a>
</body>
</html>
```
## 6. Restart the Server
After adding static files, restart Django server:
```
python manage.py runserver
```
# Django Template Language (Jinja) Guide

Django uses a built-in template engine that is **Jinja-like**.  
It allows writing **dynamic HTML** using variables, conditions, loops, and template inheritance.

---

## 1. What is Jinja / Django Template Language?

Jinja (in Django context) is used to:
- Display dynamic data in HTML
- Reuse HTML code
- Apply logic (if, for, etc.) inside templates
- Keep Python logic separate from HTML

Syntax uses:
```
{{ }} → variables
{% %} → logic / tags
{# #} → comments
```

# Tailwind CSS Setup in Django Using django-tailwind (With Reload)

This guide explains how to integrate **Tailwind CSS** into a Django project using  
`django-tailwind` and `django-browser-reload` with **automatic reload support**.

---

## 1. Install Required Python Packages

Run these commands inside your Django project (virtual environment recommended):

```bash
pip install django-tailwind
pip install django-browser-reload
```

2. Add Apps to INSTALLED_APPS

Open settings.py and update INSTALLED_APPS:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tailwind',
    'theme',                   # Tailwind app (will be created)
    'django_browser_reload',   # Auto reload

    'mycrudapp',
]
```

## 3. Create Tailwind App
Run:
```
python manage.py tailwind init

You will be asked for an app name.
Enter:
[theme]
```
This creates a Tailwind app inside your project.

## 4. Install Tailwind Dependencies (npm)

Run:
```
python manage.py tailwind install
```
This will:

Install Node dependencies

Create package.json

Setup Tailwind config automatically

## 5. Configure NPM Path in settings.py (IMPORTANT)

If npm is not detected automatically (common on Windows), add this to settings.py:
```
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
```

📌 Check npm path using:
```bash
where npm
```

## 6. Configure Template Reload Middleware
Add middleware at the bottom of MIDDLEWARE:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django_browser_reload.middleware.BrowserReloadMiddleware',
]
```
## 7. Add Reload URLs
Open urls.py (project level):
```python
from django.urls import path, include

urlpatterns = [
    path('__reload__/', include('django_browser_reload.urls')),
    path('', include('mycrudapp.urls')),
]
```

## 8. Configure Templates (Required)

In settings.py, ensure APP_DIRS is enabled:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## 9. Load Tailwind in Base Template
Edit templates/mycrudapp/base.html:
```
{% load static tailwind_tags %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Django Tailwind{% endblock %}</title>
    {% tailwind_css %}
</head>
<body>

{% block content %}{% endblock %}

</body>
</html>
```
## 10. Start Tailwind Watcher (AUTO RELOAD)

Run this command in Terminal 1:
```
python manage.py tailwind start
```
## 11. Start Django Server

Run in Terminal 2:
```
python manage.py runserver
```
Open:
```
http://127.0.0.1:8000/
```


