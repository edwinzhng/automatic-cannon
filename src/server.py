import socket
import time

def startServer(servoX, servoY, servoT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "192.168.43.104"
    port = 12345
    s.bind((host, port))

    print("Starting server...")
    s.listen(5)
    c, addr = s.accept()
    print("Got connection from", addr)

    while True:
        data = c.recv(port)
        if data == "down":
            c.send("Moving servoY " + data)
            print(data)
            servoY.adjustAngle(-5)
        elif data == "up":
            c.send("Moving servoY " + data)
            print(data)
            servoY.adjustAngle(5)
        elif data == "left":
            c.send("Moving servoX " + data)
            print(data)
            servoX.adjustAngle(-5)
        elif data == "right":
            c.send("Moving servoX " + data)
            print(data)
            servoX.adjustAngle(5)
        elif data == "fire":
            c.send("Firing now!")
            servoT.lock()
            time.sleep(2)
            servoT.unlock()
        elif data == "esc":
            c.send("Closing server, goodbye.")
            print("Exiting manual control")
            break;
    s.close()
