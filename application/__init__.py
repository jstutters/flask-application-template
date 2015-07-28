import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
if 'APPLICATION_SETTINGS' in os.environ:
    app.config.from_envvar('APPLICATION_SETTINGS')
else:
    app.config.from_object('application.default_config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    """Return a 404 error page when a URL does not exist"""
    return render_template('404.html'), 404


@app.errorhandler(401)
def permission_denied(error):
    """Return a 401 error page when access to a page is forbidden"""
    return render_template('401.html'), 401


# import submodules as blueprints here
# e.g.
#from application.users.views import mod as users_module
#app.register_blueprint(users_module)
