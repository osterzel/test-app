from flask import Flask
import os

app = Flask(__name__)

value = os.getenv('VALUE', 'Welcome to the world')

@app.route('/')
def hello_world():
    return value 

if __name__ == '__main__':
    app.run()
