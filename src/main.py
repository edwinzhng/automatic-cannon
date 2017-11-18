from PIL import Image
import cv2
import picamera
import requests
import base64
import RPi.GPIO as GPIO
#from server import startServer
from time import sleep
from trajectory import calcFinalAngles

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def camera():
	camera = picamera.PiCamera()
	camera.resolution = (720, 720)
	camera.vflip = True
	camera.capture('../data/data.jpg')
	camera.close()

	with open("../data/data.jpg", "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())

	print("imaged captured, sending to server...")
	r = requests.post("http://52.14.199.236/save.php", data={'content': encoded_string})
	print(r.content)
	print("calculating trajectory...")
	return calcFinalAngles()

class Servo():
	def __init__(self, PIN):
		self.PIN = PIN
		GPIO.setup(self.PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(self.PIN, 50)
		self.pwm.start(7.5)
		self.angle = 0

	def setAngle(self, angle):
		self.angle = 0.053*angle + 2.2
		self.pwm.ChangeDutyCycle(self.angle)

	def adjustAngle(self, angle):
		self.setAngle(self.angle + angle)

	def stop(self):
		self.pwm.stop()

	def lock(self):
		self.setAngle(0)

	def unlock(self):
		self.setAngle(180)


def loop():
	lock = False
	while True:
		new_angle = input("enter angle (-1 to auto target, -2 to lock/fire, -3 to control servoX, -4 for remote keyboard control): ")
		if(new_angle == -1):
			angles = camera()
			print("")
			print("angleX: ", angles[0])
			print("angleY: ", angles[1])
			servoY.setAngle(angles[0])
			servoX.setAngle(angles[1])
			print("target locked")
		elif(new_angle == -2):
			if(lock):
				servoT.lock()
				print("locked")
			else:
				servoT.unlock()
				print("unlocked")
			lock = not lock
		elif(new_angle == -3):
			servoX.setAngle(input("servoX angle: "))
		elif(new_angle == -4):
			startServer()
		else:
			servoY.setAngle(new_angle)


if __name__ == '__main__':		# Program start from here
	try:
		servoX = Servo(18)
		servoT = Servo(17)
		servoY = Servo(23)
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		servoY.stop()
		GPIO.cleanup()
