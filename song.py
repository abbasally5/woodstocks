from midiutil.MidiFile import MIDIFile
import os, csv
"""
# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "stocksong")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

pitch = 60           # C4 (middle C)
time = 0             # start on beat 0
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 64           # E4
time = 2             # start on beat 2
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

pitch = 67           # G4
time = 4             # start on beat 4
duration = 1         # 1 beat long
mf.addNote(track, channel, pitch, time, duration, volume)

# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
"""
def get_pitch(close):
	num = int(round(close))
	return num % 87 + 21

def convert_to_song(file_name):
	
	mf = MIDIFile(1)
	track = 0

	time = 0
	mf.addTempo(track, time, 240)

	channel = 0
	volume = 100
	
	file_loc = os.path.join(os.getcwd(), file_name+'.csv')
	with open(file_loc, "rb") as csvfile:
		reader = csv.reader(csvfile)
		reader = list(reader)
		"""
		row_count = sum(1 for row in reader)
		for i in range(1, row_count):
			print reader[i]
		"""
		i = 1
		while i < len(reader):
		#for i in range(1, len(reader)):
			close = reader[i][4]
			pitch = get_pitch(float(close))
			time += 1
			duration = 1
			mf.addNote(track, channel, pitch, time, duration, volume)
			i += 100
			print i

	with open('static/' + file_name + '.mid', 'wb') as outf:
		mf.writeFile(outf)
	outf.close()



#convert_to_song("stock.csv", "AAPL")

