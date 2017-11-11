package main

import (
	"fmt"
	"net"
	"github.com/eiannone/keyboard"
)

func main() {
	// connect to this socket
	conn, _ := net.Dial("tcp", "EDWIN-XPS15:12345")
	buf2 := make([]byte, 1024)
	err := keyboard.Open()
	if err != nil {
		panic(err)
	}

	msg := "none"

	defer keyboard.Close()
	defer conn.Close()

	fmt.Println("Press ESC to quit")
	for {
		char, key, err := keyboard.GetKey()
		if (err != nil) {
			panic(err)
		} else if (key == keyboard.KeyEsc) {
			break
		} else if (key == keyboard.KeyArrowDown) {
			msg = "down"
		} else if (key == keyboard.KeyArrowUp) {
			msg = "up"
		} else if (key == keyboard.KeyArrowLeft) {
			msg = "left"
		} else if (key == keyboard.KeyArrowRight) {
			msg = "right"
		}
		fmt.Printf("You pressed: %q\r\n", char)

		buf := []byte(msg)
		_, err = conn.Write(buf) // Write a message to the server
		msg = "none"
		// listen for reply
		//allocating memory for each integer
		n, err := conn.Read(buf2) // Read a message from the server
		if err != nil {
			fmt.Println("Error:", err)
		} else {
			_ = n
			fmt.Printf("%s\n", buf2[0:n])
		}

		if err != nil {
			fmt.Println(msg, err)
		}
	}
}
