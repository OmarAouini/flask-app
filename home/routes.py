from flask import Blueprint, render_template

home_blueprint = Blueprint('home_blueprint', __name__)

@home_blueprint.route('/home')
#@login_required
def home():
    return render_template('home/home.html', nome="pippo")
