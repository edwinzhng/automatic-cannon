import socket
import time
import constants as c

# start listening at port 12345 on the Raspberry Pi for manual controls
def startServer(servoX, servoY, servoT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((c.host, c.port))

    print("Starting server...")
    s.listen(5)
    conn, addr = s.accept()
    print("Got connection from", addr)

    # loop controls until exited by user
    while True:
        data = conn.recv(c.port)
        currentAngleX = (servoX.angle - 2.2) / 0.053
        currentAngleY = (servoY.angle - 2.2) / 0.053
        if data == "down":
            conn.send("Moving servoY " + data)
            print(data)
            servoY.setAngle(currentAngleY - 5)
        elif data == "up":
            conn.send("Moving servoY " + data)
            print(data)
            servoY.setAngle(currentAngleY + 5)
        elif data == "left":
            conn.send("Moving servoX " + data)
            print(data)
            servoX.setAngle(currentAngleX - 5)
        elif data == "right":
            conn.send("Moving servoX " + data)
            print(data)
            servoX.setAngle(currentAngleX + 5)
        elif data == "fire":
            if servoT.locked:
                print("reloading")
                conn.send("Readying cannon!")
		servoT.toggleLock()
                servoT.locked = False
            else:
                print("firing")
                conn.send("Firing now!")
		servoT.toggleLock()
                servoT.locked = True
        elif data == "esc":
            conn.send("Closing server, goodbye.")
            print("Exiting manual control")
            break;
        else:
            print("none")
            conn.send("No input")

    s.close()
