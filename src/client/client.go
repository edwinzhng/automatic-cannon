package main

import (
	"fmt"
	"net"
	"github.com/eiannone/keyboard"
)

// error check
func CheckError(err error) bool {
	if err != nil {
		fmt.Println("Error: ", err)
		return true;
	}
	return false;
}

func main() {
	// connect to this address
	addr := "192.168.43.104:12345"
	conn, _ := net.Dial("tcp", addr)
	buf2 := make([]byte, 1024)
	err := keyboard.Open()
	CheckError(err)

	msg := "none"
	fmt.Println("Connection: ", conn)

	defer keyboard.Close()
	status := true
	fmt.Println("ARROW KEYS to move, SPACE to fire, ESC to quit")
	for status {
		char, key, err := keyboard.GetKey()
		if (!CheckError(err)) {
			switch key {
			case keyboard.KeyEsc:
				msg = "esc"
				buf := []byte(msg)
				_, err = conn.Write(buf) // Write a message to the server
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
		// fmt.Printf("You pressed: %q\r\n", char)

		buf := []byte(msg)
		_, err = conn.Write(buf) // Write a message to the server
		CheckError(err)
		// listen for reply
		//allocating memory for each integer
		n, err := conn.Read(buf2) // Read a message from the server
		if (!CheckError(err)) {
			_ = n
			fmt.Printf("%s\n", buf2[0:n])
		}
		CheckError(err)
	}
	conn.Close()
}
