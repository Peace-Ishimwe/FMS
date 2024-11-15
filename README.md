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
To get started with this project, clone the repository and set up the necessary dependencies.

### Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
