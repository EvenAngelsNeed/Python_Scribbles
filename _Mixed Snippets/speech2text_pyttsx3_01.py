# python 3

# requires pywin32

import pyttsx3
import re

# Initialize the engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

system_voice = engine.getProperty("voice")


# Get current global system voice id (integer). Not same as the voice we may set here or default voice.

for i, each in enumerate(voices):

	if str(system_voice) in str(each):
		system_voice = i


def speak(text, voice = system_voice, rate = None, volume = None):

	# Set voice:
	engine.setProperty('voice', voices[voice].id)  # Selecting a female voice

	# Adjust speaking rate:
	engine.setProperty('rate', rate)

	# Adjust volume:
	engine.setProperty('volume', volume)

	print(text)

	# Make the engine speak:
	engine.say(text)

	engine.runAndWait() # Needed after each output - before another.

	engine.stop()



def voice_info():

	current_voice = engine.getProperty("voice")

	print()

	print(f"You have {len(voices)} voices installed:\n")

	for i, each in enumerate(voices):

		each_voice = re.search("name=(.*?)\n", str(each)).group(1)

		if str(current_voice) in str(each):
			#current_voice = i, re.search("name=(.*?)\n", str(each)).group(1)
			test = "* Current System Wide Voice."

		else:
			test = ""

		print("", i, each_voice, test)


	print(f'\n Current speaking rate: {engine.getProperty("rate")}')

	print(f' Current volume level: {engine.getProperty("volume")}')



# Make the engine speak:

# speak(text, voice (interger) rate (interger), volume = (float))


voice_info() # Get info about Current System Voices.

print("\n------------------\n")

speak("Hello World")

speak("How are you?", 0, 120, 1.5)

speak("Have a nice day!", 1, 250, 0.5)


# Standard usage uses default voice & settings:

engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


# Stop the engine
engine.stop()

input("\n\nEnter To Exit")