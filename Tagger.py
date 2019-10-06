from mutagen.easyid3 import EasyID3

print("")

songnam = input("What is the song name, without the .mp3 suffix?: ")

print("")

sngnm = songnam + ".mp3"

audio = EasyID3(sngnm)

audio['artist'] = u"artist"
audio['album'] = u"album"
audio['title'] = u"title"

audio.save()

print("Tagging finished. Thank you.")

print("")

