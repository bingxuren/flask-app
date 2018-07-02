from fask import Flask
app = Flask(__name__)

@app.route('/'):
def index():
    return 'index page for demo app'
