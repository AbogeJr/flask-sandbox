from myapp import app
from myapp.forms import RegistrationForm, LoginForm
from myapp.models import User, Post    
from flask import render_template, url_for, flash, redirect


# Home Page
@app.route("/")
def home():
    return render_template('home.html', title="Home")


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
