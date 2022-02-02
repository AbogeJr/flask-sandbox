from flask import Flask, render_template
app = Flask(__name__)

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

@app.route("/")
def hello_world():
    return render_template('home.html', posts=posts, title="Home")

@app.route("/about")
def about():
    return render_template('about.html', title="About")    

if __name__ == '__main__':
    app.run(debug=True)
