from flask import Flask
from flask import render_template, request, jsonify
from flask import redirect, url_for, send_file, send_from_directory
import soundcloud

app = Flask(__name__)
global client

@app.route("/")
def login():
	global client
	client = soundcloud.Client(client_id='cc4fcdc677e79e8c82ef4cb2d43305e3', 
							   client_secret='e574ea8a433d47e8ba849364094e1819',
							   redirect_uri='http://localhost:5000/index')
	print client

	"""
	print 'a'
	print client.exchange_token(code=request.args['code'])
	access_token, expires, scope, refresh_token = client.exchange_token(code=request.args['code'])
	code = params['code']
	print code
	access_token = client.exchange_token(code)
	print access_token
	"""

	return redirect(client.authorize_url())

@app.route("/index")
def hello(code=None):
	print 'index'
	code = request.args['code']
	print code
	global client
	access_token = client.exchange_token(code)
	"""
	access_token, expires, scope, refresh_token = client.exchange_token(
    code=request.args['code'])
	"""
	print 'a'
	print client.get('/me').username
	return "Hi There, %s" % client.get('/me').username
	"""
	print 'index'

	code = params['code']
	access_token = client.exchange_token(code)
	print 'a'
	print code
	print 'b'
	print access_token

	return render_template('index.html')
	"""

if __name__ == "__main__":
	app.run()