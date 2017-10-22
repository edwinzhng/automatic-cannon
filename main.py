import picamera
import requests
from PIL import Image
import RPi.GPIO as GPIO
from time import sleep

SERVO = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)		# Numbers GPIOs by physical location
GPIO.setup(SERVO, GPIO.OUT)
pwm = GPIO.PWM(SERVO, 50)
pwm.start(7.5)
	
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
    while True:
        pwm.ChangeDutyCycle(5)
        sleep(1)
        pwm.ChangeDutyCycle(7.5)
        sleep(1)

if __name__ == '__main__':		# Program start from here
	try:
		loop()
	except KeyboardInterrupt:	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

