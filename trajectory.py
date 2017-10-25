import json
import math

import '../main.py' servo
import '../faceDetection.py' as fd
s
focal_length = 2570
average_width = 0.22

def parseJson():
    data = fd.getFaceDimensions()

# calculates horizontal distance from camera based on focal length obtained from
# testing and using average width of a known object
def calcDistX(coordinates, focal_length, average_width):
    dist_x = (averageWidth * focal_length) / coordinates[0]) # horizontal distance = known width * focal length / pixel width
    return dist_x

# calculates Ep of the spring using a k value determined through experimentation
def springPotential(k, x):
    potential = 0.5*k*x*x
    return potential

# calculate projectile launch time assuming no air resistance for now
def calcTime(spring_potential, dist_x, mass):
    v_initial = math.sqrt(2*spring_potential*weight)
    time = distX
    return time

# returns vertical distance relative to cannon
def calcDistY(top, bottom, viewport_angle):
    # TODO calculate vertical distance

# returns angle needed for the projectile to hit the target
def calcAngle():
    #TODO return the angle needed

def main():
    coordinates = parseJson()
    print(coordinates[0])

if __name__ == '__main__':
    main()
