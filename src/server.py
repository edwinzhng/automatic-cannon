import socket

def startServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))

    s.listen(5)
    c, addr = s.accept()
    print ("Got connection from", addr)

    while True:
        data = c.recv(port)
        if data == "down":
            c.send("Moving servoY " + data)
            print(data)
            #servoY.setAngle(ServoY.angle - 5)
        elif data == "up":
            c.send("Moving servoY " + data)
            print(data)
            #servoY.setAngle(ServoY.angle + 5)
        elif data == "left":
            c.send("Moving servoX " + data)
            print(data)
            servoX.setAngle(ServoX.angle - 5)
        elif data == "right":
            c.send("Moving servoX " + data)
            print(data)
            #servoX.setAngle(ServoX.angle + 5)
        elif data == "fire":
            c.send("Firing now!")
            #servoT.unlock()
        elif data == "esc":
            c.send("Closing server, goodbye.")
            print("Exiting manual control")
            break;
    s.close()
