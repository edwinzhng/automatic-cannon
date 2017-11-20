import json
import math
import faceDetection as fd
import constants as c

# returns spring potential energy
def spring_potential(k, x):
    return 0.5*k*x*x

# calculates horizontal distance from camera based on c.ratio obtained from
# testing and using average width of a known object
def calcDistX(coordinates, ratio, average_width):
    dist_x = (c.average_width * c.ratio) / coordinates['width'] # horizontal distance = known width * ratio / pixel width
    return dist_x


# returns vertical distance relative to cannon
def calcDistY(coordinates, dist_x, average_width, angle):
    dist_y = math.sin(angle) * dist_x; # calculate vertical height from center of screen
    dist_y += ((c.img_height / 2) - (coordinates['center']['y'] - 50)) / c.ratio # account for vertical distance from center of screen
    return dist_y


# returns angle needed for the projectile to hit the target using
# kinematics, trigonometry, and projectile motion formulas
def calcAngleY(dist_x, dist_y, mass, k, x):
    theta = 0
    eps = spring_potential(k, x)
    v_i = math.sqrt(2*eps/mass)
    print(str(v_i) + ' - vi')

    discriminant = (math.pow(v_i, 4)-(c.g*(c.g*dist_x*dist_x+2*dist_y*v_i*v_i)))
    if discriminant < 0:
        return -1

    theta1 = math.atan((v_i*v_i + math.sqrt(discriminant)) / (c.g * x)) * 180 / math.pi
    theta2 = math.atan((v_i*v_i - math.sqrt(discriminant)) / (c.g * x)) * 180 / math.pi
    # print(str(theta1) + " - theta1")
    # print(str(theta2) + " - theta2")

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
    metersPerPixel = c.average_width / coordinates['width']
    return (coordinates['center']['x'] - c.img_width/2.0) * metersPerPixel

# return the angle needed to move horizontally, assuming 0 is
# when the cannon is horizontally facing left and rotates clockwise
def calcAngleX(dist_x, offsetX):
    angle_from_center = math.atan(-offsetX/dist_x)*180/math.pi
    return 90 + angle_from_center


# returns final results for horizontal and vertial angles from image
def calcFinalAngles(angle):
    coordinates = fd.getFaceDimensions()
    dist_x = calcDistX(coordinates, c.ratio, c.average_width)
    dist_y = calcDistY(coordinates, dist_x, c.average_width, angle)
    offsetX = calcOffsetX(coordinates)
    theta_x = calcAngleX(dist_x, offsetX)
    theta_y = calcAngleY(dist_x, dist_y, c.mass, c.k, c.x)
    return [round(theta_x), round(theta_y)]


# testing purposes
def main():
    coordinates = fd.getFaceDimensions()
    print(str(coordinates['width']) + ' - width')
    dist_x = calcDistX(coordinates, c.ratio, c.average_width)
    print (str(dist_x) + ' - horizontal distance')
    dist_y = calcDistY(coordinates, dist_x, c.average_width, 45)
    print (str(dist_y) + ' - vertical distance')
    theta = calcFinalAngles(45)
    print theta[0], theta[1]
    return theta

if __name__ == '__main__':
    main()
