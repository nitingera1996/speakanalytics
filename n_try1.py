import speech_recognition
# import pyttsx

# speech_engine = pyttsx.init('sapi5') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
# speech_engine.setProperty('rate', 150)

def speak(text):
	print text
	# speech_engine.say(text)
	# speech_engine.runAndWait()

recognizer = speech_recognition.Recognizer()

def listen():
	with speech_recognition.Microphone() as source:
		recognizer.adjust_for_ambient_noise(source)
		audio = recognizer.listen(source)

	try:
		return recognizer.recognize_google(audio)
		# or: return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return ""

import webbrowser

	# url = 'http://docs.python.org/'

	# MacOS
chrome_path = '/usr/bin/google-chrome %s'
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

while(1):
	speak("Say something!")

	# Windows
	# chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

	# Linux

	input1=listen()
	speak("I heard you say " + input1)

	# listen()
	try:
		print input1[:6]
		if input1[:4]=="open":
			url="http://"+input1[5:]+".com"
			print url
			webbrowser.get(chrome_path).open(url)
		elif input[:6]=="search":
			url=input1[7:]
			webbrowser.get(chrome_path).open(url)
	except:
		pass

