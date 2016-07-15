from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/generic')
def generic():
	return render_template('generic.html')

@app.route('/elements')
def elements():
	return render_template('elements.html')



if __name__ == '__main__':
	port = int(os.environment.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
