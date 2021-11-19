from flask import Flask, render_template

app = Flask(__name__)

posts = [

    {
        'author': 'Ogundeyi Boluwatife',
        'title': 'Blog Post One',
        'content': 'Testing out the posts functionality',
        'date': 'November 19, 2020'
    },


    {
        'author': 'Olasunkanmi Jesuferanmi',
        'title': 'Blog Post Two',
        'content': 'Testing out the posts functionality',
        'date': 'November 19, 2020'
    },

     
     {
        'author': 'Oladoke Eniola',
        'title': 'Blog Post Three',
        'content': 'Testing out the posts functionality',
        'date': 'November 19, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")

if __name__ == "__main__":
    app.run()
