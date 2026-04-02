# DjangoMosh

A Django learning project with multiple apps, MySQL support, debug toolbar integration, browser reload support, and app-level static assets.

## Tech Stack

- Python 3.14
- Django 6.0.3
- MySQL
- `python-decouple` for environment variables
- `django-debug-toolbar` for request/debug inspection
- `django-browser-reload` for auto refresh during development

## Project Structure

- `djangomosh/` - project settings, root URL config, WSGI/ASGI entry points
- `playground/` - main app, templates, and static files
- `store/` - store-related models and views
- `tags/` - tag-related models and views
- `likes/` - like-related models and views
- `manage.py` - Django command-line entry point

## Static Files

This project does not use a root-level `static/` folder. The active static assets live under:

- `playground/static/css/style.css`

The settings file is configured with:

```python
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "playground" / "static"]
```

That means template references like this work correctly:

```html
{% load static %} <link rel="stylesheet" href="{% static 'css/style.css' %}" />
```

If you add more CSS, JavaScript, or images, place them inside `playground/static/` so Django can find them automatically in development.

## Requirements

Install dependencies from `requirements.txt`. The file pins the project packages used in this workspace, including Django, MySQL support, debug toolbar, browser reload, and the supporting libraries already listed there.

## Step-by-Step Setup

### 1. Clone the repository

```bash
git clone <your-github-repo-url>
cd DjangoMosh
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If `mysqlclient` gives you trouble on Windows, make sure you are using a Python version that matches the available wheel or install the required build tools for MySQL client packages.

### 4. Create your local `.env` file

Create a file named `.env` in the project root with the variables expected by `djangomosh/settings.py`:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_NAME=django_test
DATABASE_USER=root
DATABASE_PASSWORD=root
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

Notes:

- `SECRET_KEY` must be unique for your machine and should not be committed.
- `DEBUG=True` is fine for local development only.
- Update the MySQL values if your local database uses a different user, password, host, or port.

### 5. Create the MySQL database

Make sure MySQL is running, then create the database referenced in `.env`.

Example:

```sql
CREATE DATABASE django_test;
```

If you use a different database name, update `DATABASE_NAME` in `.env` to match.

### 6. Run migrations

```bash
python manage.py migrate
```

This creates the Django tables and applies the app migrations already included in the repository.

### 7. Create an admin user

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

### 8. Start the development server

```bash
python manage.py runserver
```

Open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/admin/`
- `http://127.0.0.1:8000/__debug__/` for Django Debug Toolbar
- `http://127.0.0.1:8000/__reload__/` for browser reload support

## Useful Django Commands

- `python manage.py check` - verify the project configuration
- `python manage.py makemigrations` - create new migrations after model changes
- `python manage.py migrate` - apply migrations
- `python manage.py runserver` - start the local server
- `python manage.py createsuperuser` - create an admin account

## Development Notes

- The project uses `python-decouple` to read settings from environment variables.
- `DEBUG_TOOLBAR` is enabled through `INSTALLED_APPS` and middleware.
- `django-browser-reload` is enabled for automatic page refresh in development.
- The project URL config includes the main app, admin, debug toolbar, and browser reload routes.

## Troubleshooting

### `ImportError: No module named 'decouple'`

Install dependencies into the active virtual environment:

```bash
pip install -r requirements.txt
```

### `ImportError: Couldn't import Django`

Make sure the virtual environment is activated and `django` is installed in that same environment.

### MySQL connection errors

Check that:

- MySQL is running
- The database exists
- The username and password in `.env` are correct
- `DATABASE_HOST` and `DATABASE_PORT` match your local MySQL server

### Static files not loading

Confirm your templates use:

```html
{% load static %} <link rel="stylesheet" href="{% static 'css/style.css' %}" />
```

and that the file exists at:

- `playground/static/css/style.css`

## Notes for Production

- Set `DEBUG=False`
- Use a strong `SECRET_KEY`
- Use production database credentials
- Run `python manage.py collectstatic` before deploying static assets
