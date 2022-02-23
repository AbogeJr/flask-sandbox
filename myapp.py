from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c968502a61da53471f4fd0fcb148cada'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(30), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profile_pic}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.content}', '{self.date_posted}')"
    

# # Dummy Data
# posts = [
#     {
#         'author':'John Doe',
#         'title': 'Post One',
#         'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
#         'date_posted': 'May 7, 2021'
#     },
#     {
#         'author':'Jane Doe',
#         'title': 'Post Two',
#         'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
#         'date_posted': 'May 8, 2021'
#     },
#     {
#         'author':'Jim Halpert',
#         'title': 'Post Three',
#         'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
#         'date_posted': 'May 8, 2021'
#     },
#     {
#         'author':'Pam Beasley',
#         'title': 'Post Four',
#         'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
#         'date_posted': 'May 8, 2021'
#     },
#     {
#         'author':'Michael Scott',
#         'title': 'Post Five',
#         'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
#         'date_posted': 'May 8, 2021'
#     }
# ]


# Home Page
@app.route("/")
def home():
    return render_template('home.html', posts=posts, title="Home")


# About Page
@app.route("/about")
def about():
    return render_template('about.html', title="About")    


# Registration Page
@app.route("/registration", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account successfully created for { form.username.data }', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Registration", form=form)


# Login Page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@aboge.com' and form.password.data == 'admin':
            flash(f'Admin logged in successfully! Welcome Boss.', 'success')
            return redirect(url_for('home'))
        else:
             flash(f'Access Denied! Please check credentials.', 'danger')   
    return render_template('login.html', title="Login", form=form, methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(debug=True)
