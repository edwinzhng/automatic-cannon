import picamera
import requests
from PIL import Image
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)		# Numbers GPIOs by physical location


class Servo:
	def __init__(self, PIN):
		self.PIN = PIN
		GPIO.setup(self.PIN, GPIO.OUT)
		self.pwm = GPIO.PWM(self.PIN, 50)
		self.pwm.start(5)
		self.reset()

	def rotate(self, angle):
		self.pwm.changeDutyCycle((1/18 * (angle+90) + 2))

	def reset(self):
		self.rotate(0)
	
def destroy():
	pwm.stop()
	GPIO.cleanup()			# Release resource

##def camera():
##	camera = picamera.PiCamera()
##	camera.resolution = (3280, 2464)
##	camera.capture('image.jpeg')
##	img = Image.open('image.jpeg').rotate(180)
##	img.save('image.jpeg')
##
##	#r = requests.post("http://52.15.34.99:8081", data={'content': fileIn, 'name': "ocr.jpeg"})
##	print("image taken")
##	camera.close()
##	GPIO.output(LED3, ON)
##	GPIO.output(LED2, OFF)

def loop():
	servoY = Servo(18)
	servoX = Servo(17)
    while True:
    	servoY.reset()
    	sleep(1)
    	servoY.rotate(90)
    	sleep(1)
    	servoY.rotate(-90)

if __name__ == '__main__':		# Program start from here
	try:
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

