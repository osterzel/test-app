from flask import Flask
import os

application = Flask(__name__)

value = os.getenv('VALUE', 'Welcome to the world')

@application.route('/')
def hello_world():
    return value 

if __name__ == '__main__':
    application.run()
