from flask import Blueprint
from flask import Request, render_template

frontend_bp = Blueprint("frontend", __name__)

@frontend_bp.get("/")
def index():
    return render_template("index.html")