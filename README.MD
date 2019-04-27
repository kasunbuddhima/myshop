# myshop project configuration

# developed environment
- Python 3.5
- Django 2.1
- Postgresql database


# steps

- First of all make sure a virtual environment is created and it is activated
$ virtualenv venv -p python3
$ source venv/bin/activate

- Create myshop_settings.ini file in somewhere safe inside the development pc to protect password credentials
e.g /etc/settings/myshop_settings.ini

And fill database details and secret key as following

```
[database]
DATABASE_USER: username
DATABASE_PASSWORD: password
DATABASE_HOST: localhost
DATABASE_PORT: 5432
DATABASE_ENGINE: databse_engine
DATABASE_NAME: database_name

[secrets]
SECRET_KEY: django_secret_key
```

- Project settings structure

```
settings/
	__init__.py
	base.py     default settings (universal to all environments)
	local.py    local development environment specific details (should be gitignored)
	dev.py      (should be gitignored)
	prod.py     (should be gitignored)
```

Go inside myshop directory

- Install requirements
```
(myshop)$ pip install -r requirements.txt
```

- Create static files
```
(myshop)$ ./manage.py collectstatic --settings=myshop.settings.local
```

- Create migrations
```
(myshop)$ ./manage.py makemigrations --settings=myshop.settings.local
```

- Migrate
```
(myshop)$ ./manage.py migrate --settings=myshop.settings.local
```

- Create a super user
```
(myshop)$ ./manage.py createsuperuser --settings=myshop.settings.local
```

- Run server
```
(myshop)$ ./manage.py runserver --settings=myshop.settings.local
```

create a new product short_info accessing dashboard
http://localhost:8000/dashboard/


Assignment

- Expanded fields in product model
is_active = models.BooleanField(default=False, help_text='indicates whether products is active or not')
short_info = models.TextField(blank=True, null=True, help_text='short details about product')

- custom product detail view
/templates/catalogue/details.html (short info is included)



ref:
https://github.com/django-oscar/django-oscar






