import json
import math

# import main
import faceDetection as fd

img_width = 720 # img width in pixels
ratio = 760 # ratio needed to get horizontal distance
average_width = 0.13 # average width of human head
k = 100 # TODO need to experiment with different masses to find true k
x = 0.2 # amount that the spring compresses
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
def calcDistY(coordinates, dist_x):
    # TODO return vertical distance somehow using the viewport angle, dist_x and
    # distance from the center of the face to the floor
    # (need to work out how to determine where the floor is)
    dist_y = 0.4
    return dist_y

# returns angle needed for the projectile to hit the target using
# kinematics, trigonometry, and projectile motion formulas
def calcAngle(dist_x, dist_y, mass, k, x):
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
    return theta

# returns how far from the center the face is (horizontally)
# positive value means too far right, negative means too far left
def calcOffsetX(coordinates):
    return coordinates['center']['x'] - img_width

def calcFinalAngle():
    coordinates = fd.getFaceDimensions()
    dist_x = calcDistX(coordinates, ratio, average_width)
    dist_y = calcDistY(coordinates, dist_x)
    theta = calcAngle(dist_x, dist_y, mass, k, x)
    return theta

# def main():
#     coordinates = fd.getFaceDimensions()
#     print(str(coordinates['width']) + ' - width')
#     dist_x = calcDistX(coordinates, ratio, average_width)
#     print (str(dist_x) + ' - horizontal distance')
#     dist_y = calcDistY(coordinates, dist_x)
#     theta = calcAngle(dist_x, dist_y, mass, k, x)
#     offset_x = calcOffsetX(coordinates)
#     print theta
#     return theta

# if __name__ == '__main__':
#     main()
