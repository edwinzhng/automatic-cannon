# Define global constants

# Image values in pixels
img_width = 1680      # image width in pixels
img_height = 1050     # image height in pixels

# Details for face detection API
api_key = "n3vg0dfc4j42o0ap4b54mm0msg"
api_secret = "l20v0d9j4a7bnb7lqcqps7rddm"
img_url = "http://52.14.199.236/data.jpg" #AWS IP

# Trajectory calculation constants
ratio = 760           # ratio of pixels to m needed for horizontal distance
average_width = 0.13  # average width of human head
k = 30                # experimental spring constant
x = 0.07              # amount that the spring compresses
mass = 0.005          # mass of the projectile being fired
g = 9.81

# Socket constants for server
host = "192.168.43.104"
port = 12345
