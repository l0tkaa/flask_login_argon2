from flask import Flask, render_template
from config import Config 
from routes.auth import auth
from models.user import db
from routes.api import api

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all() #creates db tables


app.register_blueprint(auth)
app.register_blueprint(api, url_prefix = '/api')

@app.route('/')
def home():
    return render_template('home.html') # create a home.html template for home page

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)



