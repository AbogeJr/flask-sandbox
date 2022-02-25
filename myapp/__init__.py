from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from myapp.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c968502a61da53471f4fd0fcb148cada'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from myapp import routes