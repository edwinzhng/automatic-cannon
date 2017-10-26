from PIL import Image
import requests
import base64
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def camera():
	camera = picamera.PiCamera()
	camera.resolution = (720, 720)
	camera.capture('data.jpg')
	camera.close()

	with open("../data/data.jpg", "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())

	print("posting image...")
	r = requests.post("http://18.221.15.32/save.php", data={'content': encoded_string})
	print(r.content)

class Servo():
	def __init__(self, PIN):
		self.PIN = PIN
		GPIO.setup(self.PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(self.PIN, 50)
		self.pwm.start(7.5)
		self.angle = 0
		
	def setAngle(self, angle):
		self.pwm.ChangeDutyCycle(0.053*angle + 2.2)
		
	def stop(self):
		self.pwm.stop()

	def adjust(self, y):
		self.adjustAngle(angle + y)

def loop():
	while True:
		newAngle = input("angle (-1 to take picture): ")
		if(newAngle == -1):
			camera()
		else:
			servoY.setAngle(newAngle)


if __name__ == '__main__':		# Program start from here
	try:
		servoY = Servo(18)
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		servoY.stop()
		GPIO.cleanup()
