from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required
from models.user import User, db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from forms import RegistrationForm
import bcrypt

# Create the blueprint
auth = Blueprint('auth', __name__)

# Set up Login Manager
login_manager = LoginManager()


# Define Login Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user.password.encode('utf-8')):
            # Password is correct, proceed with login
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    return render_template('login.html', form=form)

# Define logout route
@auth.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

         # Hash the user's password using bcrypt
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        # Create a new user instance with the hashed password
        new_user = User(username=form.username.data, password=hashed_password)
        
        # Add the new user to the session and commit to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('auth.login'))


    return render_template('register.html', form=form) #create register.html template 

@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
