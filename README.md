# Fundraising Management System

A Django-based Fundraising Management System designed to help users create and fund various campaigns. This project is designed with role-based authentication and offers administrative controls for managing users and monitoring funding activities across different sectors. The system includes a clean and responsive user interface built with Tailwind CSS.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Author](#author)

## Project Overview
The Fundraising Management System provides users with a platform to create and support campaigns within predefined sectors such as agriculture, trading, and others. Each user has a role that determines their permissions:
- **Admin**: Can create campaigns, manage users, assign roles, and view reports.
- **User**: Can fund campaigns and view their funding history.

## Features
### Authentication
- **Role-based Access**: Supports both admin and user roles.
- **First User as Admin**: The first registered user becomes an admin by default and can assign roles to other users.

### Campaign Management
- **Admin Privileges**: Admins can create, view, and manage campaigns.
- **User Privileges**: Users can fund campaigns and track their funding history.

### Profile Management
- Users can manage their profiles with fields such as first name, last name, email, phone number, province, sector, and role.

### Dashboard & Reporting
- **Admin Dashboard**: Offers user and funding activity management, including sector-based funding reports.
- **User Dashboard**: Displays personal funding activities and impact.

### Responsive UI
- Built with Tailwind CSS to ensure a responsive and clean design.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: Tailwind CSS
- **Database**: PostgreSQL
- **Libraries**: Django templating system, Tailwind CSS (via CDN)

## Installation

1. Clone the repository:
git clone https://github.com/peace-ishimwe/FMS.git
cd fundraising-management-system

2. Create a virtual environment and activate it:
bash
Copy code
python -m venv env
# For Windows
env\Scripts\activate
# For macOS/Linux
source env/bin/activate

3. Install the required dependencies:
bash
Copy code
pip install -r requirements.txt

4. Install and configure Tailwind CSS:
bash
Copy code
npm install -g tailwindcss
tailwindcss init

5. Run Tailwind CSS to watch for changes in styles:
bash
Copy code
tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch

## Database Setup
Create a PostgreSQL database:
sql
Copy code
CREATE DATABASE fundraising_db;

Update the DATABASES section in the settings.py file:
python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fundraising_db',
        'USER': 'your_postgresql_username',
        'PASSWORD': 'your_postgresql_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Apply migrations:
bash
Copy code
python manage.py makemigrations
python manage.py migrate

Create a superuser for admin access:
bash
Copy code
python manage.py createsuperuser

## Usage
Start the development server:
bash
Copy code
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000.

Log in using the superuser credentials or register as a new user.


## Author: Munyaneza Ishimwe Peace