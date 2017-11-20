import socket
import time
import constants as c

# start listening at port 12345 on the Raspberry Pi for manual controls
def startServer(servoX, servoY, servoT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.43.104"
    port = 12345
    s.bind((c.host, c.port))

    print("Starting server...")
    s.listen(5)
    c, addr = s.accept()
    print("Got connection from", addr)

    # loop controls until exited by user
    while True:
        data = c.recv(c.port)
        currentAngleX = (servoX.angle - 2.2) / 0.053
        currentAngleY = (servoY.angle - 2.2) / 0.053
        if data == "down":
            c.send("Moving servoY " + data)
            print(data)
            servoY.setAngle(currentAngleY - 5)
        elif data == "up":
            c.send("Moving servoY " + data)
            print(data)
            servoY.setAngle(currentAngleY + 5)
        elif data == "left":
            c.send("Moving servoX " + data)
            print(data)
            servoX.setAngle(currentAngleX - 5)
        elif data == "right":
            c.send("Moving servoX " + data)
            print(data)
            servoX.setAngle(currentAngleX + 5)
        elif data == "fire":
            if servoT.locked:
                print("reloading")
                c.send("Readying cannon!")
                servoT.locked = False
            else:
                print("firing")
                c.send("Firing now!")
                servoT.locked = True
            servoT.toggleLock()
        elif data == "esc":
            c.send("Closing server, goodbye.")
            print("Exiting manual control")
            break;
        else:
            print("none")
            c.send("No input")

    s.close()
