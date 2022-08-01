from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/art')
def art():
    # Art.main()
    #return render_template('a432.html')
    return render_template("art.html")


@views.route('/resume')
def resume():
    # Art.main()
    #return render_template('a432.html')
    return render_template("index.html")
