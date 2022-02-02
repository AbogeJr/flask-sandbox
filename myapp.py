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
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')    

if __name__ == '__main__':
    app.run(debug=True)
