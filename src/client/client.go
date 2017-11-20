package main

import (
	"fmt"
	"net"
	"github.com/eiannone/keyboard"
)

// print and check error
func CheckError(err error) bool {
	if err != nil {
		fmt.Println("Error: ", err)
		return true;
	}
	return false;
}

// returns message and status
func HandleInput(conn net.Conn, status bool) (string, bool) {
	msg := "none"

	// loop to send keyboard controls
	char, key, err := keyboard.GetKey()
	if (!CheckError(err)) {
		switch key {
		case keyboard.KeyEsc:
			msg = "esc"
			status = false
		case keyboard.KeyArrowDown:
			msg = "down"
		case keyboard.KeyArrowUp:
			msg = "up"
    case keyboard.KeyArrowLeft:
			msg = "left"
		case keyboard.KeyArrowRight:
			msg = "right"
		case keyboard.KeySpace:
			msg = "fire"
		default:
			msg = "none"
		}
	}

	_ = char

	return msg, status
}

func main() {
	// open connection to this address and port
	addr := "192.168.43.104:12345"
	conn, _ := net.Dial("tcp", addr)
	fmt.Println("Connection: ", conn)

	buf2 := make([]byte, 1024)
	msg := "none"
	status := true

	// allow keyboard input
	err := keyboard.Open()
	CheckError(err)
	defer keyboard.Close()
	fmt.Println("ARROW KEYS to move, SPACE to fire, ESC to quit")

	for status {
		// take input from keyboard
		msg, status = HandleInput(conn, status)
		buf := []byte(msg)
		_, err = conn.Write(buf) // Write a message to the server
		CheckError(err)

		// listening allocating byte array for server reply
		n, err := conn.Read(buf2)
		if (!CheckError(err)) {
			_ = n
			fmt.Printf("%s\n", buf2[0:n])
		}
		CheckError(err)
	}
	conn.Close()
}
