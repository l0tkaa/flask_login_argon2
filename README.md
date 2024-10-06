# Simple Flask Login Form

## Overview

My Flask App is a simple web application built using Flask, Flask-WTF for form handling, and Flask-Login for user authentication. This app demonstrates how to create a basic user authentication system with login and logout functionality.

## Features

- User login and logout functionality
- Simple user interface with forms
- Uses Flask-WTF for form handling
- User session management with Flask-Login
- Ability to register new users
- form validation
- hashed and salted passwords with bcrypt

## Technologies Used

- Python
- Flask
- Flask-WTF - Form Handling
- Flask-Login - Session management
- SQLAlchemy - Database ORM
- Bcrypt - Password encryption

## Installation

### Prerequisites

- Python 3.6 or later [python.org](https://www.python.org/downloads/).
- pip (Python package installer)

### Clone the Repository

1. Clone this repository to your local machine using:

```bash
git clone https://github.com/l0tkaa/flask_login_bcrypt.git
cd flask_login_bcrypt
```
2. Create a virtual environment and activate it
``` bash 
python -m venv venv
```
3. Install required packages
``` bash
pip install -r requirements.txt
```
4. Set up the database
``` bash
python
>>> from app import db
>>> db.create_all()
```
6. Run the application
``` bash
python app.py
```
The app will run in a browser on localhost.

### Documentation
[Flask](https://flask.palletsprojects.com/en/3.0.x/)
[Flask-Login](https://flask-login.readthedocs.io/en/latest/)
[Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/)
[SQLAlchemy](https://www.sqlalchemy.org/)
[Bcrypt](https://pypi.org/project/bcrypt/)
[Argon2-cffi](https://pypi.org/project/argon2-cffi/)