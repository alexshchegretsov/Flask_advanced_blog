from flask_blog import app, bcrypt, db
from flask import render_template, redirect, flash, url_for
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import User, Post

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
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to Log In', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessfull', 'danger')
    return render_template('login.html', title='Login', form=form)
