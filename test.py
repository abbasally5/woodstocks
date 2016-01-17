from flask import Flask
from flask import render_template, request, jsonify
from flask import redirect, url_for, send_file, send_from_directory
import soundcloud

app = Flask(__name__)
global client
global access_token
global user

@app.route("/")
def login():
	global client
	client = soundcloud.Client(client_id='cc4fcdc677e79e8c82ef4cb2d43305e3', 
							   client_secret='e574ea8a433d47e8ba849364094e1819',
							   redirect_uri='http://localhost:5000/index')
	print client

	return redirect(client.authorize_url())

@app.route("/index")
def hello(code=None):
	print 'index'
	code = request.args['code']
	global client
	global access_token
	access_token = client.exchange_token(code)
	print "Username = %s" % client.get('/me').username

	global user
	user = client.get('/me')
	print user.id


	try:
		# get a tracks oembed data
		track_url = 'http://soundcloud.com/forss/flickermood'
		embed_info = client.get('/oembed', url=track_url)
		print 'a'
		# print the html for the player widget
		#return embed_info.html
	except Exception as e:
		print e

	try:
		print user.public_favorites_count
	except Exception as e:
		print e
	try:
		tracks = client.get('/users/'+str(user.id)+'/favorites')
		for track in tracks:
			print track.title
			print track.uri
			print track.permalink_url
			embed_info = client.get('/oembed', url=track.permalink_url)

			#print embed_info['html']
			return track.stream_url

	except Exception as e:
		print e
	try:
		print client.get('/users/'+str(user.id)+'/playlist_likes')
	except Exception as e:
		print e

	return render_template('index.html', data=access_token)

if __name__ == "__main__":
	app.run()