from flask import Flask, render_template
from werkzeug.wsgi import SharedDataMiddleware
import os

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# store assets files on server for now
# can be accessed at /static/path
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
	'/': os.path.join(os.path.dirname(__file__), 'assets')
})

if __name__ == '__main__':
	app.run()
