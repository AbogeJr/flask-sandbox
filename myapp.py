from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c968502a61da53471f4fd0fcb148cada'

# Garbage Data
posts = [
    {
        'author':'John Doe',
        'title': 'Post One',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
        'date_posted': 'May 7, 2021'
    },
    {
        'author':'Jane Doe',
        'title': 'Post Two',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
        'date_posted': 'May 8, 2021'
    },
    {
        'author':'Jim Halpert',
        'title': 'Post Three',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
        'date_posted': 'May 8, 2021'
    },
    {
        'author':'Pam Beasley',
        'title': 'Post Four',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
        'date_posted': 'May 8, 2021'
    },
    {
        'author':'Michael Scott',
        'title': 'Post Five',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et ipsa ex itaque? Explicabo adipisci amet corrupti, nobis, ipsa, nam minus tempore aspernatur alias neque earum laboriosam consequuntur excepturi nisi expedita!',
        'date_posted': 'May 8, 2021'
    }
]


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
