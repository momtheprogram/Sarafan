# Sarafan project's Backend

### Description:
A test task. The backend of the grocery store project.

### Start up project:

-   Clone the repository and go to it on the command line:
```bash
git clone https://github.com/momtheprogram/api_rating_genres.git

cd api_yamdb
```
-   Create and activate a virtual environment.

-   Windows:
```bash
python -m venv venv

. venv/Scripts/activate
```

Linux/macOS:
```bash
python3 -m venv venv

source venv/bin/activate
```

-   Install dependencies from a file requirements.txt:

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

-   Perform migrations:

```bash
python manage.py migrate
```

-   Start project:

```bash
python manage.py runserver
```

### Documentation:
http://127.0.0.1:8000/redoc/


### Login to the admin panel
log: 'admin'\
pass: '654321'
