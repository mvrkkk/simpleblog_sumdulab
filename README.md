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

### To run on your local machine follow this steps:

#### Option 1: manual

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

#### Option 2: Using docker

1)  ensure that u have installed Docker app on your local machine. If not - download docker app & follow the installation instructions

Docker desktop: https://www.docker.com/products/docker-desktop/
Installation instructions:
- MacOS: https://docs.docker.com/desktop/install/mac-install/
- Linux: https://docs.docker.com/desktop/install/linux-install/
- Windows (WSL backend): https://docs.docker.com/desktop/install/windows-install/

After installation - run Docker desktop app

2) Next, clone this repo:
```bash
git clone https://github.com/mvrkkk/simpleblog_sumdulab.git
```

2) Navigate to repository folder
```
cd ~/simpleblog_sumdulab
```

3) Build your own docker image on local machine
```
docker build . -t django_sumdu -f Dockerfile
```
4) After image has been create - run application by executing
```
docker run -d django_sumdu -p 8000:8000
```

Our web application is accessible via http://127.0.0.1:8000/
