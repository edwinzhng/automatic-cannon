from PIL import Image
import picamera
import requests
import base64
import RPi.GPIO as GPIO
from time import sleep
from trajectory import calcFinalAngle

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def camera():
	camera = picamera.PiCamera()
	camera.resolution = (720, 720)
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
		self.pwm.ChangeDutyCycle(0.053*angle + 2.2)

	def stop(self):
		self.pwm.stop()

	def adjust(self, y):
		self.setAngle(angle + y)

	def.lock(self):
		self.setAngle(0)

	def.unlock(self).setAngle(180)

def loop():
	while True:
		new_angle = input("enter angle (-1 to auto target, -2 to fire, -3 to control): ")
		if(new_angle == -1):
			angles = camera()
			print("")
			print("angleX: ", angles[0])
			print("angleY: ", angles[1])
			servoY.setAngle(angle[0])
			print("target locked")
		elif(new_angle == -2):
			servoT.lock()
		elif(new_angle == -3):
			while True:
				key = cv2.waitKey(1) & 0xFF
			    if key == 0:
			        print "up"
			    elif key == 1:
			        print "down"
			    elif key == 2:
			        print "left"
			    elif key == 3:
			        print "right"
			    print key
		else:
			servoY.setAngle(newAngle)


if __name__ == '__main__':		# Program start from here
	try:
		servoY = Servo(18)
		servoT = Servo(17)
		servoX = Servo(23)
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		servoY.stop()
		GPIO.cleanup()
