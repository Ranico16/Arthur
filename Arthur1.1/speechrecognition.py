import speech_recognition as sr
from os import path

AUDIO_FILE = " MyAudioFile.wav"

r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source)
	
try:
	print (" Did you say " + r.recognize_sphinx(audio))

except sr.UnknownValueError:
	print ("I did not understand what you said")

except sr.RequestError as e:
	print ("Encountered an error; {0}".format(e))
