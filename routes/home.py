from flask import Blueprint, render_template,url_for

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')