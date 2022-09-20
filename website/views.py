from flask import Blueprint, render_template, send_file
from .Art import Svg, ArtConfig

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", html_file='/Art/embeddedArt.html')


@views.route('/art')
def art():
    svg = Svg(ArtConfig(count=2000),
              "./website/templates/Art/GeneratedArtSVG.html")
    svg.make_svg()

    return render_template("randomArt.html",
                           html_file='/Art/GeneratedArtSVG.html')


@views.route('/resume')
def resume():
    #return render_template('a432.html')
    return send_file('static/MatthewCurtisResume.pdf', as_attachment=True)
