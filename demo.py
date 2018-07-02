from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page for demo app'

@app.route('/graphql')
def graphql():
    result = schema.execute('{ hello }')
    print(result.data(['hello']))
app.view_functions['graphql'] = GraphQLView.as_view('graphql', schema=schema, graphql=True)
