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