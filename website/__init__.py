# makes a website a  python package - we can import it
#seting flask
from flask import Flask

def create_app():
    app = Flask(__name__) #represents the name of the file
    app.config['SECRECT_KEY'] = '4234t2345' # must set a secret key for an app
    
    #we have to tell flask, that we have some blueprints here are they
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') # all the urls we get with a prefix

    return app