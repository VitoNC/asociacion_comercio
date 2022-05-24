# Getting started

(On a Windows based environment)

## Dependencies needed for installation
- Python 3
- Django's Pillow library

## Install and run Wagtail

### Install dependencies
In order to check that te Python package is installed.
```bash
$ python3 --version
```

### Create and activate a virtual environment
In order to isolate the installed dependecies from other projects.
```bash
$ python3 --m venv env
$ env\Scripts\activate
```

### Install Wagtail
```bash
$ pip install wagtail
```

### Generate your site
```bash
$ wagtail start "my_project_name"
```

### Install project dependencies
```bash
$ cd "my_project_name"
$ pip install -r requirements.txt
```

### Create database
```bash
$ python manage.py migrate
```

### Create an admin user
```bash
$ python manage.py createsuperuser
```

### Start the server
```bash
$ python manage.py runserver
```
> Note: In your browser:`http://localhost:8000`.

This should show the Wagtail welcome page, and the deployment is finished.


