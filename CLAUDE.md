# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django-based vehicle maintenance tracking application ("Carnet d'entretien") that allows users to manage vehicles, owners, and maintenance records. The application is configured for French locale (fr-fr timezone: Europe/Paris).

## Development Setup

**Dependencies**: Uses Pipenv for dependency management
```bash
pipenv install          # Install dependencies
pipenv shell           # Activate virtual environment
```

**Database**: Uses Supabase (PostgreSQL) for both development and production via DATABASE_URL

**Development Server**:
```bash
python manage.py runserver    # Start development server
```

**Database Management**:
```bash
python manage.py makemigrations    # Create migration files
python manage.py migrate           # Apply migrations
python manage.py createsuperuser   # Create admin user
```

## Architecture

### Core Django Apps

- **entretiens**: Maintenance records with PDF invoice upload validation
- **vehicules**: Vehicle management with image uploads and technical specifications  
- **proprietaires**: Vehicle owners contact information
- **users**: Custom user model extending AbstractUser
- **dashbaord**: Dashboard functionality (note: typo in directory name)
- **config**: Django project settings and URL configuration

### Data Model Relationships

- `Proprietaire` (1) -> (N) `Vehicule` -> (N) `Entretien`
- Custom `CustomUser` model with email as unique field
- File uploads: PDF invoices for maintenance, images for vehicles

### Key Features

- **Django Baton**: Enhanced admin interface (replaces default Django admin)
- **Media Handling**: Configured for file uploads with proper validation
- **Multi-language**: French locale with custom formatting (e.g., Euro currency formatting with spaces and commas)
- **Custom Validators**: PDF-only validation for maintenance invoices
- **Supabase Integration**: PostgreSQL database hosted on Supabase

### File Structure Notes

- `config/`: Django project configuration (not app-specific)
- `media/`: User uploads (factures/, photos/)
- `static/`: Static files (CSS)
- `templates/`: Django templates with base.html
- `models/`: Contains UI mockups/prototypes (not Django models)
- `dashbaord/`: Dashboard app (note: directory name has typo)

### Database Configuration

Uses Supabase PostgreSQL database for both development and production environments. Database connection configured via `DATABASE_URL` environment variable with `dj-database-url`.

### Environment Variables

Requires `.env` file with:
- `SECRET_KEY`: Django secret key
- `DATABASE_URL`: Supabase PostgreSQL connection string

### Architecture du projet

Ce projet utilise des vues basées sur les classes pour structurer et gérer les différentes interfaces et composants. Cette approche permet une meilleure organisation, réutilisabilité et maintenabilité du code.


## Instructions spécifiques ou directives

### Directives techniques

Le projet adopte une architecture orientée objet avec des vues basées sur les classes pour faciliter la gestion des interactions et des composants.