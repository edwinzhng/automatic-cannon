from PIL import Image
import picamera
import time
import requests
import base64
import RPi.GPIO as GPIO
from server import startServer
from time import sleep
from trajectory import calcFinalAngles

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def camera():
	camera = picamera.PiCamera()
	camera.resolution = (1680, 1050)
	camera.vflip = True
        camera.start_preview()
	camera.capture('../data/data.jpg')
	camera.close()

	with open("../data/data.jpg", "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())

	print("Image captured, sending to server...")
	r = requests.post("http://52.14.199.236/save.php", data={'content': encoded_string})
	print(r.content)
	print("Calculating trajectory...")
	return calcFinalAngles(((servoY.angle - 2.2) / 0.053))


# servo definition with functions
class Servo():
	def __init__(self, PIN):
		self.PIN = PIN
		GPIO.setup(self.PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(self.PIN, 50)
		self.pwm.start(7.5)
		self.angle = 0
                self.locked = False

	# set servo to specific angle
	def setAngle(self, angle):
		self.angle = 0.053*angle + 2.2
		self.pwm.ChangeDutyCycle(self.angle)

    # adjust angle of servo
	def adjustAngle(self, angle):
		self.setAngle(self.angle + angle)

    # stop servo
	def stop(self):
		self.pwm.stop()

    # lock servo and fire
	def lock(self):
		self.setAngle(0)
                self.locked = 1

	# unlock servo to be ready to fire
	def unlock(self):
		self.setAngle(180)
                self.lock = 0
                self.locked = 0

        def toggleLock(self):
                if (self.locked):
                    self.unlock()
                else:
                    self.lock()


# loop options
def loop():
	lock = False
	while True:
		new_angle = input("Enter angle (-1 to auto target, -2 to lock/fire, -3 to control servoX, -4 for remote keyboard control): ")
		if(new_angle == -1):
			angles = camera()
                        servoT.lock()
			print("")
			print("AngleX: ", angles[0])
			print("AngleY: ", angles[1])
			if angles[1] == -1:
				print("Target is too far away!")
				continue
			servoX.setAngle(angles[0])
			servoY.setAngle(angles[1])
			print("Target locked!")
                        time.sleep(2)
                        servoT.toggleLock()
			print("Fire!")
		elif(new_angle == -2):
                        servoT.toggleLock()
		elif(new_angle == -3):
			servoX.setAngle(input("ServoX angle: "))
		elif(new_angle == -4):
			startServer(servoX, servoY, servoT)
		else:
			try:
				val = int(new_angle)
				servoY.setAngle(val % 91) # set as input angle mod 91
			except ValueError:
				print("Please enter a valid integer!")
				continue


# start program
if __name__ == '__main__':
	try:
		servoX = Servo(18)
		servoT = Servo(17)
		servoY = Servo(23)
		servoX.setAngle(90)
		servoY.setAngle(30)
		servoT.unlock()
		loop()
	except KeyboardInterrupt:	# exit loop when 'Ctrl+C' is pressed
		servoY.stop()
		GPIO.cleanup()
