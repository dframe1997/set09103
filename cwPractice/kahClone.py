from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def host():
	return 'User'

@app.route('/host')
def user():
	start = '<img src="'
	url = url_for('static',filename='kahoot.jpg')
	end = '">'
	return 'Host' + start+url+end, 200
