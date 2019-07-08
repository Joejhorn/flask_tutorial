from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from flask import request
app = Flask(__name__)
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

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/user/<name>')
def user(name):
  return render_template('user.html', name=name)





