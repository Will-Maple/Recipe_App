# Recipe App (Django)
A Django web app for recipes (<a href="#">Seen Here</a>). Users can register/login to create, favorite, and search thru various user created recipes! 
<br>
<br>

<img src="#" width=70% alt="Image of app"> 

## Tech-stack
- Django 
- Python
- Virtual Environments

## Steps to Run 

### Clone repo
- Of course!


### Set Up Environment
https://www.python.org/downloads/windows/ - And add to PATH
```sh
 python --version
 pip -- version
```
Install and set up Virtual Environment
```sh
 pip install virtualenvwrapper-win
 mkvirtualenv <name>
 workon <name>
```
### Set Up Database
Install MySQL and create a user...
<a href="https://www.mysql.com/">Link to MySQL site.</a>

Create a database in the MySQL client
```sql
CREATE DATABASE your_db_name CHARACTER SET UTF8MB4;
CREATE USER 'your_db_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_db_name.* TO 'your_db_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Update in settings.py the DATABASES object with your database config
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
...
...
    }
}
```

### Set up Server
Install Django
```sh
pip install django
```
Run Server
```sh
py manage.py runserver
```
