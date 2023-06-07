## Blog web-application project
Author: Stakan Mark, IHm-23 group

## Tech stack:
```
Python
Django
JavaScript
SQLite
Crispy forms
Bootsrap4
```

# To run on your local machine follow this steps:

1) Clone github repository; Open terminal (bash/shell (MacOS/Linux) or git-bash/powershell (Windows) if git installed & type
```shell
git clone https://github.com/mvrkkk/simpleblog_sumdulab.git
```

2) Create virtual environment. For running project without any issues `conda` is recommended:
```
conda create --name django_blogproject python=3.8 --no-default-packages && conda activate django_blogproject
```

3) Install dependencies:
```
pip install -r requirements.txt
```

4) After all dependencies installed, while in root directory of repo execute in terminal:
```
python3 manage.py makemigrations # initialize a database
python3 manage.py migrate # create objects in database
```

5) Finaly, start web-application by typing:
```
python3 manage.py runserver
```

If done correctly without any issues, web-application is accessible via 8000 port of localhost.
Open your browser & navigate to `http://127.0.0.1:8000/`
