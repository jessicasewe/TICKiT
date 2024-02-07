from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")
  
@auth.route("/logout")
def logout():
    return render_template("login.html")

@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('signupUsername')
        email = request.form.get('signupEmail')
        password = request.form.get('signupPassword')

        if len(username) < 3:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be atleast 7 characters.', category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.tickit'))

    return render_template("signup.html")