# DjangoMosh

A Django learning project with multiple apps, MySQL support, debug toolbar integration, browser reload support, and app-level static assets.

## What You Need

- Python 3.14
- MySQL installed and running
- Git installed

## Project Files

- `manage.py` - Django command-line entry point
- `djangomosh/` - project settings, URL config, WSGI/ASGI entry points
- `playground/` - main app, templates, and static files
- `store/` - store-related models and views
- `tags/` - tag-related models and views
- `likes/` - like-related models and views
- `.env.example` - sample environment file
- `.gitignore` - ignores local files, secrets, caches, and virtual environments

## Static Files

Static files live in the app-level folder:

- `playground/static/css/style.css`

The project is configured with:

```python
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "playground" / "static"]
```

That means your templates should load CSS like this:

```html
{% load static %} <link rel="stylesheet" href="{% static 'css/style.css' %}" />
```

## Dependencies

Install packages from `requirements.txt`.

This project uses:

- `Django`
- `python-decouple`
- `django-debug-toolbar`
- `django-browser-reload`
- `mysqlclient`

## Step-by-Step Setup

### 1. Clone the repository

```bash
git clone <your-github-repo-url>
cd DjangoMosh
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
```

macOS/Linux:

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install project dependencies

```bash
pip install -r requirements.txt
```

If `mysqlclient` fails on Windows, make sure your Python version matches the available wheel, or install the MySQL build tools required for that package.

### 6. Create your `.env` file

Copy `.env.example` to `.env`, then edit the values for your machine.

Example `.env`:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_NAME=django_test
DATABASE_USER=root
DATABASE_PASSWORD=root
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

Important:

- Do not commit `.env`
- Keep `SECRET_KEY` private
- Change the database values if your local MySQL setup is different

### 7. Create the MySQL database

Log in to MySQL and create the database used in `.env`.

```sql
CREATE DATABASE django_test;
```

If you choose another database name, update `DATABASE_NAME` in `.env`.

### 8. Run Django migrations

```bash
python manage.py migrate
```

### 9. Create an admin user

```bash
python manage.py createsuperuser
```

### 10. Start the development server

```bash
python manage.py runserver
```

Open these URLs in your browser:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/admin/`
- `http://127.0.0.1:8000/__debug__/`
- `http://127.0.0.1:8000/__reload__/`

## Example Workflow After Cloning

```bash
git clone <your-github-repo-url>
cd DjangoMosh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Common Commands

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Development Notes

- `python-decouple` reads settings from environment variables in `djangomosh/settings.py`
- `django-debug-toolbar` is enabled in `INSTALLED_APPS` and `MIDDLEWARE`
- `django-browser-reload` is enabled for development refresh
- `.gitignore` excludes `.env`, `.venv/`, caches, logs, and build artifacts

## Troubleshooting

### `ImportError: No module named 'decouple'`

```bash
pip install -r requirements.txt
```

### `ImportError: Couldn't import Django`

Activate the correct virtual environment and install dependencies again.

### MySQL connection errors

Check that:

- MySQL is running
- The database exists
- The username and password in `.env` are correct
- `DATABASE_HOST` and `DATABASE_PORT` match your local MySQL server

### Static files not loading

Make sure your template uses:

```html
{% load static %} <link rel="stylesheet" href="{% static 'css/style.css' %}" />
```

and that the file exists at:

- `playground/static/css/style.css`

## Production Notes

- Set `DEBUG=False`
- Use a strong `SECRET_KEY`
- Use production database credentials
- Run `python manage.py collectstatic` before deployment
