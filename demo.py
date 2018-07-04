from flask import Flask
from .schema import schema
from .data import setup
import json

app = Flask(__name__)

setup()

@app.route('/')
def index():
    return 'index page for demo app'


@app.route('/developer')
def developer():
    query = '''
        {
            developer(id: "1000") {
                name
            }
        }
    '''
    result = schema.execute(query)
    return json.dumps(result.data['developer'])


@app.route('/manager')
def manager():
    query = '''
        {
            manager(id: "2000") {
                id
                name
                teammates {
                    name
                }
                role
            }
        }
    '''
    result = schema.execute(query)
    return json.dumps(result.data['manager'])