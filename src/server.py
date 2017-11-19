import socket

def startServer(servoX, servoY, servoT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.43.104"
    port = 12345
    s.bind((host, port))

    print
    s.listen(5)
    c, addr = s.accept()
    print("Got connection from", addr)

    while True:
        data = c.recv(port)
        if data == "down":
            c.send("Moving servoY " + data)
            print(data)
            servoY.setAngle(servoY.angle - 5)
        elif data == "up":
            c.send("Moving servoY " + data)
            print(data)
            servoY.setAngle(servoY.angle + 5)
        elif data == "left":
            c.send("Moving servoX " + data)
            print(data)
            servoX.setAngle(servoX.angle - 5)
        elif data == "right":
            c.send("Moving servoX " + data)
            print(data)
            servoX.setAngle(servoX.angle + 5)
        elif data == "fire":
            c.send("Firing now!")
            servoT.lock()
        elif data == "esc":
            c.send("Closing server, goodbye.")
            print("Exiting manual control")
            break;
    s.close()
