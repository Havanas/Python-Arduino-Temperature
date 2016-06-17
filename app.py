import os
from flask import Flask

app = Flask(__name__)

print(os.environ['APP_SETTINGS'])

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()