import sys, termios, tty, os, time
 
while True:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if (ch == "a"):
        print("Left pressed")
    elif (ch == "d"):
        print("Right pressed")
    elif (ch == "w"):
        print("Up pressed")
    elif (ch == "s"):
        print("Down pressed")
    elif (ch == "k"):
        break
