from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        "author": "Abdullahi Husain",
        "title": "Blog Post",
        "content": "My First blog post",
        "date_posted": "April 18, 2024"
    },
    {
        "author": "Asiyah Aliyu",
        "title": "Blog Post 32",
        "content": "My 32nd blog post",
        "date_posted": "April 18, 2021"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

if __name__ == "__main__":
    app.run(debug=True)
