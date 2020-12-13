
import random

intent = raw_input(":")



greet = [ "Hello!", "Hello, How are you", "Hi", "Hi, How can I help you?", "Hi, What's up?"]
name = ["My name is Arthur", "I am Arthur", "You can call me Arthur", "I am an Artificial Intelligence Assistant called Arthur"]





if (intent == "Hi"):
	print (random.choice(greet))

if (intent == "name"):
	print(random.choice(name))
	

