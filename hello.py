from flask import Flask,render_template


# Create a Flask Intance
app = Flask(__name__)


# Create a route decorator
@app.route('/')

# def index():
  # return "<h1>Hello World</h1>"
  
  

#  FLITERS!!!
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags


def index():
  name = "Yaseen"
  stuff = "This is Bold Text"
  favorite_pizza = ['Pepperoni','chees','Meshrooms',41]
  return render_template('index.html',first_name = name, stuff=stuff,favorite_pizza=favorite_pizza)



# http://127.0.0.1:5000/user/Yaseen
# @app.route('/user/<name>')
# def user(name):
#   return "<h1>Hello {}</h1>".format(name)

@app.route('/user/<name>')
def user(name):
  return render_template('user.html',name=name)




# Create Custome Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
  return render_template('500.html'), 404