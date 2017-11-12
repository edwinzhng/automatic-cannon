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
        # TODO move servo with this code
        if data == "down":
            c.send("Moving servoY " + data)
        elif data == "up":
            c.send("Moving servoY " + data)
        elif data == "left":
            c.send("Moving servoX " + data)
        elif data == "right":
            c.send("Moving servoX " + data)
        elif data == "fire":
            c.send("Firing now!")
        elif data == "esc":
            c.send("Closing server, goodbye.")
            print("Exiting manual control")
            break;

    s.close()

if __name__ == '__main__':
    startServer()
