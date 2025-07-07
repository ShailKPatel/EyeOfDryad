from flask import Blueprint, render_template
from .forms import UserForm
from .models import User, db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", form=UserForm(), users=User.query.all())
