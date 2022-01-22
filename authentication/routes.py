from flask import Blueprint, flash, redirect, render_template, url_for
from .forms import LoginForm

authentication_blueprint = Blueprint('authentication_blueprint', __name__)

@authentication_blueprint.route('/')
def route_default():
    return redirect(url_for('authentication_blueprint.login'))

@authentication_blueprint.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # user check logic
        if form.user_name.data == 'admin' and form.password.data == 'admin':
            flash('login successful')
            return redirect('home')
    return render_template('authentication/login.html', form=form)

@authentication_blueprint.route('/signup')
def signup():
    return render_template('authentication/signup.html')