import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

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
                self.locked = 0
	
	# toggle locked position
        def toggleLock(self):
                if (self.locked):
                    self.unlock()
                else:
                    self.lock()
