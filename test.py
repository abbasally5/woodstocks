from flask import Flask
from flask import render_template, request, jsonify
from flask import redirect, url_for, send_file, send_from_directory
import soundcloud

app = Flask(__name__)

@app.route("/login")
def login():
	client = soundcloud.Client(client_id='cc4fcdc677e79e8c82ef4cb2d43305e3', 
							   client_secret='e574ea8a433d47e8ba849364094e1819',
							   redirect_uri='http://localhost:5000/')
	print client

	return redirect(client.authorize_url())

@app.route("/")
def hello():
	print 'index'
	return render_template('index.html')

if __name__ == "__main__":
	app.run()