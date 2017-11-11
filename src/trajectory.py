import json
import math
import faceDetection as fd

img_width = 720 # in pixels
img_height = 720
ratio = 760 # ratio needed to get horizontal distance
average_width = 0.13 # average width of human head
k = 20 # TODO need to experiment with different masses to find true k
x = 0.1 # amount that the spring compresses
mass = 0.005 # mass of the projectile being fired
viewport_angle = 10 # calculated viewport angle of camera
angle = 0 # TODO pass angle through from main

def spring_potential(k, x):
    return 0.5*k*x*x

# calculates horizontal distance from camera based on ratio obtained from
# testing and using average width of a known object
def calcDistX(coordinates, ratio, average_width):
    dist_x = (average_width * ratio) / coordinates['width'] # horizontal distance = known width * ratio / pixel width
    return dist_x

# returns vertical distance relative to cannon
# TODO pass in angle
def calcDistY(coordinates, dist_x, average_width):
    dist_y = math.sin(angle) * dist_x; # calculate vertical height from center of screen
    dist_y += ((img_height / 2) - (coordinates['center']['y'] - 50)) / ratio # account for vertical distance from center of screen
    return dist_y

# returns angle needed for the projectile to hit the target using
# kinematics, trigonometry, and projectile motion formulas
def calcAngleY(dist_x, dist_y, mass, k, x):
    theta = 0
    eps = spring_potential(k, x)
    v_i = math.sqrt(2*eps/mass)
    print(str(v_i) + ' - vi')
    g = 9.81
    discriminant = (math.pow(v_i, 4)-(g*(g*dist_x*dist_x+2*dist_y*v_i*v_i)))
    if discriminant < 0:
        return False
    theta1 = math.atan((v_i*v_i + math.sqrt(discriminant)) / (g * x))*180/math.pi
    theta2 = math.atan((v_i*v_i - math.sqrt(discriminant)) / (g * x))*180/math.pi
    print(str(theta1) + " - theta1")
    print(str(theta2) + " - theta2")
    if theta1 > 0 and theta1 < 45:
        theta = theta1
    else:
        theta = theta2
        if theta2 < 0:
            theta = -theta
        if theta > 45:
            theta = 90 - theta
    return theta

# returns how far from the center the face is (horizontally)
# positive value means too far right, negative means too far left
def calcOffsetX(coordinates):
    metersPerPixel = average_width / coordinates['width']
    return (coordinates['center']['x'] - img_width/2.0) * metersPerPixel

# return the angle needed to move horizontally, assuming 0 is
# when the cannon is horizontally facing left and rotates clockwise
def calcAngleX(dist_x, offsetX):
    angle_from_center = math.atan(-offsetX/dist_x)*180/math.pi
    return 90 + angle_from_center

# Changed function name and return type
def calcFinalAngles():
    coordinates = fd.getFaceDimensions()
    dist_x = calcDistX(coordinates, ratio, average_width)
    dist_y = calcDistY(coordinates, dist_x, average_width)
    offsetX = calcOffsetX(coordinates)
    theta_x = calcAngleX(dist_x, offsetX)
    theta_y = calcAngleY(dist_x, dist_y, mass, k, x)
    return [round(theta_x), round(theta_y)]

print calcFinalAngles()[0]
# for testing
'''def main():
    coordinates = fd.getFaceDimensions()
    print(str(coordinates['width']) + ' - width')
    dist_x = calcDistX(coordinates, ratio, average_width)
    print (str(dist_x) + ' - horizontal distance')
    dist_y = calcDistY(coordinates, dist_x, average_width)
    print (str(dist_y) + ' - vertical distance')
    theta = calcFinalAngles()
    print theta[0], theta[1]
    return theta

if __name__ == '__main__':
    main()'''
