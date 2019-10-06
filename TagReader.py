from mutagen.mp3 import MP3
from mutagen.id3 import ID3

print("")

songnam = input("What is the song name, without the .mp3 suffix?: ")

print("")

sngnm = songnam + ".mp3"

audio = MP3(sngnm)

print(audio.info.length)
print(audio.info.bitrate)

audio = ID3(sngnm)

print("")

print(audio['TPE1'].text[0]) #artist
print(audio['TIT2'].text[0]) #track
print(audio['TDRC'].text[0]) #release

print("")

print("Report finished. Thank you.")

print("")

