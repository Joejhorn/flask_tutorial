from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from flask import request
from flask_moment import Moment
from datetime import datetime
app = Flask(__name__)
moment = Moment(app)

# ...
bootstrap = Bootstrap(app)


# without templates

# @app.route('/')
# def index():
#   return '<h1>Hello World'

# @app.route('/joe')
# def index1():
#   return '<h1>Hello Joe Fucker'

# #Dynamic Routes
# @app.route('/joe/<lastname>')
# def last_name(lastname):
#   return (f'joe {lastname}')

#Dynamic Route with context to globally accessible object
# @app.route('/')
# def index():
#   user_agent = request.headers.get('User-Agent')
#   return '<p>Your browser is {}</p>'.format(user_agent)

#rendered pages using bootstrap and jinga
@app.route('/')
def index():
  return render_template('index.html', current_time = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)

#Custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



