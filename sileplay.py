from pydub import AudioSegment

#Params
song_path_input = "C:/ph/dlngb.mp3"
#Silent intervals
after_each_ms = 3500
#for each silent interval, for how long to silent
for_how_long_silent_ms = 5
sampled_song_outname = "test3_5s_5ms.mp3"
#

song = AudioSegment.from_mp3(song_path_input)
print song.duration_seconds
new_song = []
start = 0
while start < (song.duration_seconds * 1000):
    #print start
    new_song.append(song[start:start+after_each_ms-for_how_long_silent_ms] + AudioSegment.silent(duration=for_how_long_silent_ms))
    start = start + after_each_ms
ready_song = 0
for stream in new_song:
    ready_song += stream
ready_song.export(out_f=sampled_song_outname,format="mp3")
print ready_song.duration_seconds
