[![Django CI](https://github.com/Goldenhubuz/DjangoSQLite/actions/workflows/django.yml/badge.svg?branch=main)](https://github.com/Goldenhubuz/DjangoSQLite/actions/workflows/django.yml)
[![wakatime](https://wakatime.com/badge/user/49489c61-f548-4cec-982d-e443f9ca894f/project/b57978d6-bf53-45e7-a56e-e1efe5440226.svg)](https://wakatime.com/badge/user/49489c61-f548-4cec-982d-e443f9ca894f/project/b57978d6-bf53-45e7-a56e-e1efe5440226)

# DjangoSQLite

A simple boilerplate project for quickly setting up a Django application with SQLite.

## Overview

This project serves as a starting point for Django applications, particularly for development or small-scale use cases. It includes the basic configuration required to run a Django app with SQLite as the default database.

**Note:** This is not intended for production use. For production, consider using a more robust database like PostgreSQL and configure additional settings (e.g., security, performance, scaling).

## Features

- Django framework
- SQLite for lightweight database needs
- Clean and minimal folder structure
- Basic Makefile for automation
- Requirements file for easy dependency management

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Goldenhubuz/DjangoSQLite.git
   cd DjangoSQLite
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the app in your browser at `http://127.0.0.1:8000`.

## Folder Structure

- `config/` - Configuration files for the project.
- `manage.py` - Entry point for Django CLI commands.
- `requirements.txt` - Python dependencies for the project.
- `Makefile` - Optional automation commands for setup and development.

## Usage

This boilerplate is ideal for:

- Prototyping new features in Django
- Running quick experiments with SQLite
- Learning and testing Django concepts in a lightweight setup

## Contributing

Contributions are welcome! If you find issues or have ideas to improve this boilerplate, feel free to open an issue or submit a pull request.
