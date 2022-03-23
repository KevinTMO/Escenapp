# EscenApp
## Connecting you to your scene

EscenApp is a web application for local artists to promote their events and talents.

## Features

- Create a custom user profile via email/login
- Create events to add to your responsive profile
- Find other events created by other artists
- Simple UX design

## Tech

EscenApp uses a number of technologies to work properly:

- [ Python3 ] - Main programming language for backend
- [ Flask ] - micro web framework written in Python
- [ Nginx ] - open source software for web serving, reverse proxying, caching, load balancing, media streaming, and more
- [ Supervisor ] - client/server system that allows its users to monitor and control a number of processes on UNIX-like operating systems
- [ Bootstrap ] - great UI boilerplate for modern web apps
- [ Jinja2 ] - web template engine for the Python programming language
- [ Flask SQLAlchemy ] - extension for Flask that adds support for SQLAlchemy by providing useful defaults and extra helpers that make it easier to accomplish common tasks
- [ SQLite ] - SQLite is a database engine, written in the C language

## Installation

EscenApp requires [python3](https://www.python.org/) to run.

Install the dependencies to start.

```sh
sudo apt update
sudo apt install python3.8
sudo apt install python3-pip
pip install bcrypt==3.2.0
pip install certifi==2019.11.28
pip install cffi==1.15.0
pip install -U click==8.0.4
pip3 install email_validator
pip3 install -U Flask==2.0.3
pip3 install Flask-Bcrypt==0.7.1
pip3 install Flask-Login==0.5.0
pip3 install Flask-Mail==0.9.1
pip3 install -U Flask-SQLAlchemy==2.5.1
pip3 install Flask-WTF==1.0.0
pip3 install itsdangerous==1.1.0
pip3 install -U Jinja2==3.0.3
pip3 install MarkupSafe==2.1.0
pip3 install Pillow==7.0.0
pip3 install six==1.14.0
pip3 install SQLAlchemy==1.4.31
pip3 install -U Werkzeug==2.0.3
pip3 install -U WTForms==3.0.1
pip3 install WTForms-SQLAlchemy==0.3
```

#### Run locally

Run:

```sh
python3 run.py
```

URL
```sh
127.0.0.1:5000
```

or

```sh
localhost:5000
```

## Authors
EscenApp was created by:

| Author | Github |
| ------ | ------ |
| Kevin Ramos | [KevinTMO][Kevin] |
| Sergio Vera | [funkified][Sergio] |
| Yared Torres | [partychu][Yared] |

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [Kevin]: <https://github.com/KevinTMO>
   [Sergio]: <https://github.com/funkified>
   [Yared]: <https://github.com/partychu>
