from flask import Flask, render_template


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
	app.run(port=8080, debug=True)