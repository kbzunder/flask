# where users go to
from flask import Blueprint, render_template #to use templates 

# it has a banch of routes inside 

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
#whenever we go on a main page of a website it will runß