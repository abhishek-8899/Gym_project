Gym Management System

A full-stack web application built with Django for managing gym operations, user enrollments, attendance, and memberships. This system provides a seamless interface for users to sign up, enroll in fitness plans, track their attendance, and view gym services.

## Features

* User Authentication: Secure signup and login system using phone numbers as usernames.
* Plan Enrollment: Users can choose from various membership plans and select preferred trainers during enrollment.
* Attendance Tracking: Daily logs for workout sessions, including login/logout times and specific workout types.
* Profile Management: Personalized dashboards for users to view their enrollment status and attendance history.
* Image Gallery: Dynamic gallery to showcase gym facilities and transformations.
* Contact System: Integrated contact form for user inquiries.

## Tech Stack

* Backend: Django (Python)
* Database: SQLite (Development)
* Frontend: HTML5, CSS3, JavaScript, and Django Template Language
* Styling: Bootstrap and Custom CSS

## Project Structure

The project is organized into a core project folder and a primary application:

* `Gym_project/`: Core configuration including settings, URLs, and WSGI/ASGI configurations.
* `authapp/`: Main application handling business logic, including:
* Models: `Contact`, `Enrollment`, `Trainer`, `Membership`, `Gallery`, and `Attendence`.
* Views: Logic for handling authentication, enrollment, and attendance records.




## Setup and Installation


2. Install Django:
pip install django


3. Run Migrations:
```
python manage.py makemigrations
python manage.py migrate

```


4. Create a Superuser (for admin access):
```
python manage.py createsuperuser

```


5. Start the Server:
```
python manage.py runserver

```



Access the application at `http://127.0.0.1:8000/`.
