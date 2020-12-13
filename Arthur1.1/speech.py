import pyttsx3

def speech(audio):
	engine = pyttsx3.init()
	engine.say(audio)
	engine.runAndWait()

