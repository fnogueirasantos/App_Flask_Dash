import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from .analytics.dash_01.dashboard import create_dashboard_01
from .analytics.dash_02.dashboard import create_dashboard_02
from .analytics.dash_03.dashboard import create_dashboard_03


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

### DATABASE SETUPS
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)


#### LOGIN CONFIGS 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"


# Function to create Dash apps and set layouts
def create_dash_apps():
    # Create Dash app instances and set Flask server
    dash_app1 = create_dashboard_01(app)
    dash_app2 = create_dashboard_02(app)
    dash_app3 = create_dashboard_03(app)

    # Serve Dash assets locally
    dash_app1.scripts.config.serve_locally = True
    dash_app2.scripts.config.serve_locally = True
    dash_app3.scripts.config.serve_locally = True

    # ... (additional Dash apps)

    return dash_app1, dash_app2, dash_app3

# Call the function to create Dash apps and layouts
dash_app1, dash_app2, dash_app3 = create_dash_apps()


#### ROUTES

@app.route('/')
def home():
    return 'Página inicial do Flask'

@app.route('/dashboard1/')
def dashboard1():
    return dash_app1.index()

@app.route('/dashboard2/')
def dashboard2():
    return dash_app2.index()

@app.route('/dashboard3/')
def dashboard3():
    return dash_app3.index()