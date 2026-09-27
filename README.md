# PC Repair Tracker

A Django web application for tracking device repairs.
This project grew from a Python terminal program into a website.

## Features

- Sign in and sign out
- Create repair tickets
- View and search tickets by device name or problem
- Update statuses: Pending, In Progress, or Completed
- Store tickets in a SQLite database
- Manage records through Django admin
- Styled interface
- Automated tests for login protection and status updates

Signed-in users share the same ticket list.

## Technologies

Python, Django, SQLite, HTML, CSS, and Git.

## Run Locally

These commands are for macOS or Linux with Python 3.12 installed.

### 1. Download the project

```bash
git clone https://github.com/paukhai99/pc-repair-tracker.git
cd pc-repair-tracker
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Set up the database and a login account

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ and sign in with the account you created.

The admin page is at http://127.0.0.1:8000/admin/.

## Run Tests

```bash
python manage.py test repairs
```

The tests check that:
- Signed-out visitors are redirected to login.
- Signed-in users can save a ticket's updated status.

Tests use a separate database.

## Original Terminal Version

```bash
python main.py
```

The terminal version stores tickets in tickets.json.
It does not share data with the Django website.

## Local Configuration

The local database, ticket JSON file, and virtual environment are
excluded from Git.

Django reads its secret key from DJANGO_SECRET_KEY if set.
Otherwise, it generates a temporary key for local development,
which can require signing in again after a server restart.

This project currently uses local development settings.
Production deployment requires additional configuration.

## Future Improvements

- Record repair history
- Add more automated tests
- Deploy an online demo