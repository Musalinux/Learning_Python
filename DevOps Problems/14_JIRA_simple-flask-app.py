# we just import flask module 
from flask import Flask

# Create a flask app instance
app = Flask(__name__)

# add a decorator. This performs an action before execution of the function
@app.route("/")

# now define the function 
def hello ():
    return 'hello world'

# Flask comes with an inbuilt server, so you dont need to deploy it anywhere

app.run ('0.0.0.0')