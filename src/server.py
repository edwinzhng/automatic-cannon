import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print ('Got connection from',addr)
c.send('Send me some data!')

while True:
    data = c.recv(port)
    print data
    c.send("Recieved: " + data)

s.close()
