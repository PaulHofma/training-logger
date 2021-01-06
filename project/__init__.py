__version__ = '0.1'

from flask import Flask
from project.controllers import *

def landing_page():
    return "The is the landing page!"

app = Flask(__name__)

app.add_url_rule('/', view_func=landing_page, methods=['GET'])
app.add_url_rule('/index', view_func=index.index, methods=['GET'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
