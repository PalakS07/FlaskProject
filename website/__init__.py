from flask import Flask 

def create_app():
    app = Flask(__name__)  # Creating a Flask app
    app.config['SECRET_KEY'] = 'PALAKLAVANYA'  # Fixed typo: 'SECRATE_KEY' → 'SECRET_KEY'
    from.views import views
    from.auth import auth 

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    return app
      # Corrected indentation
