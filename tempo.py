import librosa
from librosa.beat import tempo


music_fuckign_stuff = ""

y, sr = librosa.load(music_fuckign_stuff)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print(f"{tempo}")

