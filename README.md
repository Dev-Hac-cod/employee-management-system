# employee-management-system

Step1:

Open editor: Vs code

Step2:

Create a project using 

>django-admin startproject "project name"

Step3:

Create app “employee” after change directory to “ems”

./ems> python manage.py startapp employee

Step4:

Creating superuser for admin

>python manage.py createsuperuser

Enter admin username, password

Step5: 

Apply two-step migrations

>python manage.py makemigrations
>python manage.py migrate
 
Step6:

Run using 

>python manage.py runserver

Step7:

Create models in models.py in-app “employee”

Step8:

Creating methods in views.py in-app “employee”

Step9:

Add URL to the urls.py in project folder “ems” and including “employee”
URLs here.

# Django Authentication

Installation Steps 

[CLICK HERE](https://docs.djangoproject.com/en/4.1/topics/auth/)

