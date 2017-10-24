from PIL import Image
import requests
import base64

def camera():
	# camera = picamera.PiCamera()
	# camera.resolution = (720, 720)
	# camera.capture('data.jpg')
	# img = Image.open('data.jpg')
	# img.save('data.jpg')

	with open("data.jpg", "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())
	
	print("posting image...")
	r = requests.post("http://18.221.15.32/save.php", data={'content': encoded_string})
	print(r.status_code)

camera()

# import requests
# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)

# class Servo():
# 	def __init__(self, PIN):
# 		self.PIN = PIN
# 		GPIO.setup(self.PIN, GPIO.OUT)
# 		self.pwm = GPIO.PWM(self.PIN, 50)
# 		self.pwm.start(7.5)
# 		self.angle = 0
		
# 	def setAngle(self, angle):
# 		self.pwm.ChangeDutyCycle(0.053*angle + 2.2)
		
# 	def stop(self):
# 		self.pwm.stop()

# 	def adjust(self, y):
# 		self.adjustAngle(angle + y)

# def camera():
# 	# camera = picamera.PiCamera()
# 	# camera.resolution = (720, 720)
# 	# camera.capture('data.jpg')
# 	# img = Image.open('data.jpg')
# 	# img.save('data.jpg')

# 	with open("data.jpg", "rb") as image_file:
# 		encoded_string = base64.b64encode(image_file.read())
	
# 	print("posting image...")
# 	r = requests.post("http://18.221.15.32/save.php", data={'content': encoded_string})
# 	print("image posted")
# 	#camera.close()
# 	#GPIO.output(LED3, ON)
# 	#GPIO.output(LED2, OFF)

# def loop():
# 	while True:
# 		newAngle = input("angle: ")
# 		servoY.setAngle(newAngle)

		

# if __name__ == '__main__':		# Program start from here
# 	try:
# 		servoY = Servo(18)
# 		loop()
# 	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
# 		servoY.stop()
# 		GPIO.cleanup()

