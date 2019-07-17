from flask import Flask, render_template, url_for
app = Flask(__name__)


posts = [
    {
        'author': 'Alex Shchegretsov',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April, 20, 2019'
    },
    {
        'author': 'Alexey Syryk',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'July, 17, 2019'
    }
]

@app.route('/')
def hello():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__== '__main__':
    app.run(debug=1)