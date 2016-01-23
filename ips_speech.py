import speech_recognition as sr 
import serial

PORT = '/dev/ttyACM0' # change this to your COM port number
baudrate = 9600

port = serial.Serial(PORT,baudrate,timeout = 0)

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Your Destination?(1 to 4)")
	audio = r.listen(source)

try:
	ch = r.recognize_google(audio)
	if ch == 'one':
		ch = 1
	elif ch == '2':
		ch = 2
	elif ch == '3':
		ch = 3
	elif ch == '4':
		ch = 4
	if ch in [1,2,3,4]:
		print "Your Destination ", ch
		print type(ch)
		port.write(chr(ch+48))
	else:
		print 'Enter a valid Destination'
except sr.UnknownValueError:
	print("could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))

port.close()
