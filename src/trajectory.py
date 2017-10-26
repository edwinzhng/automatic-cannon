import json
import math

import main
import faceDetection as fd

ratio = 2570 # ratio needed to get horizontal distance
average_width = 0.15 # average width of human head
k = 30 # TODO need to experiment with different masses to find true k
x = 0.3 # amount that the spring compresses
mass = 0.005 # mass of the projectile being fired
viewport_angle = 10 # calculated viewport angle of camera
height = 0.1 # distance from camera to ground

def spring_potential(k, x):
    return 0.5*k*x*x

# calculates horizontal distance from camera based on ratio obtained from
# testing and using average width of a known object
def calcDistX(coordinates, ratio, average_width):
    dist_x = (average_width * ratio) / coordinates['width']# horizontal distance = known width * ratio / pixel width
    return dist_x

# returns vertical distance relative to cannon
def calcDistY(top, bottom, viewport_angle, height):

    return dist_y

# returns angle needed for the projectile to hit the target
def calcAngle(dist_x, dist_y, mass):
    spring_potential(k, x)
    v_initial = math.sqrt(2*spring_potential*mass)

    return angle

def main():
    coordinates = fd.getFaceDimensions()            # first get coordinates of face from image
    print(coordinates['width'])                     # calculate horizontal distance based on width of head
    dist_x = calcDistX(coordinates, 2570, 0.22)
    dist_y = calcDistY(coordinates, viewport_angle)
    calcTime(spring_potential, dist_x, mass)
    return calcAngle(dist_x, dist_y, time)


if __name__ == '__main__':
    main()
