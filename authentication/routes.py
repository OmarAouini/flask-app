from flask import Blueprint, redirect, render_template, url_for

authentication_blueprint = Blueprint('authentication_blueprint', __name__)

@authentication_blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.login'))

@authentication_blueprint.route('/login')
def login():
    return render_template('authentication/login.html')

@authentication_blueprint.route('/signup')
def signup():
    return render_template('authentication/signup.html')
