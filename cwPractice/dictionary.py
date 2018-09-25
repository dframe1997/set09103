from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def redirectToHome():
	return redirect(url_for('homepage'))

@app.route('/home')
def homepage():
	return '''
		Home
		<a href="edinburgh">Edinburgh</a>
	'''

@app.route('/edinburgh')
def oxford():
	return '''
		<a href="home">Home</a>
		Edinburgh is the capital of Scotland.
	'''
