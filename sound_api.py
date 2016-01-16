import soundcloud

client = soundcloud.Client(client_id='cc4fcdc677e79e8c82ef4cb2d43305e3')

tracks = client.get('/tracks', limit=10)
for track in tracks:
	print track.title
app = client.get('/apps/124')
print app.permalink_url