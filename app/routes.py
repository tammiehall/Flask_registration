from app.blueprints.auth.models import User
from flask.helpers import url_for
import flask_login
from app import db
from flask import current_app as app, render_template, request, redirect, url_for, flash
from app.models import Post
from flask_login import login_user, logout_user, current_user

@app.route('/', methods=['GET', 'POST'])
def home():
    print(current_user if current_user else None)
    if request.method == 'POST':
        p = Post(
                body=request.form.get('body'),
                user_id=1
            )
        db.session.add(p)
        db.session.commit()
        flash('Post created successfully', 'success')
        return redirect(url_for('home'))
    context = {
        'posts': Post.query.order_by(Post.date_created.desc()).all()
    }
    # return render_template('home.html', body='This is the first post', first_name='Derek', last_name='Lang', date_posted=9)
    return render_template('home.html', **context)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # look for the user in our database
        user = User.query.filter_by(email=email).first()
        # if the email and/or password don't match,
        if user is None or not user.check_password(password):
            # show an error messages
            flash('You typed in either an incorrect email or password', 'danger')
            # redirect to the login page
            return redirect(url_for('login'))
        # otherwise
        # log the user in
        login_user(user)
        flash('You have logged in successfully!', 'info')
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out successfully', 'primary')
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form.get('password') != request.form.get('confirm_password'):
            flash('Your password do not match.', 'danger')
            return redirect(url_for('auth.login'))
        print('It works!')
        flash('User has registered succesfully', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html')
