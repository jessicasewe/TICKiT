from flask import Blueprint, render_template, request, flash, redirect, url_for, session, request, jsonify
from .models import User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .payment import create_checkout
from frontend.models import Ticket


auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                session['username'] = user.username
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.tickit'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)
  
@auth.route("/logout")
# @login_required 
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('signupUsername')
        email = request.form.get('signupEmail')
        password = request.form.get('signupPassword')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(username) < 3:
            flash('Username must be greater than 2 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(password) < 7:
            flash('Password must be atleast 7 characters.', category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.tickit'))

    return render_template("signup.html", user=current_user)

##EXPLORE PAGE
@auth.route("/explore")
def explore():
    return render_template("explore.html", user=current_user)

# welcome page
@auth.route("/welcome")
def welcome():
    return render_template("welcome.html", user=current_user)

# create_checkout
@auth.route("/create_checkout", methods=['POST'])
def checkout():
    request_data = request.get_json()
    
    order_id = request_data.get('order_id')
    item_id = request_data.get('item_id')
    product = request_data.get('product')
    currency = request_data.get('currency')
    order_total = request_data.get('order_total')
    description = request_data.get('description')
    
    response = create_checkout(order_id,item_id,product,currency,order_total,description)
    return response


#purchased tickets
@auth.route("/purchased_tickets")
def purchased_tickets():
    # Fetch the purchased ticket names from the database
    purchased_tickets = Ticket.query.with_entities(Ticket.product).filter_by(user_id=current_user.id).all()

    # Extract the product names from the fetched tickets
    ticket_names = '\n'.join([ticket.product for ticket in purchased_tickets])

    headers = {
        'Content-Type': 'application/json'
    }
    return ticket_names, 200, headers

