package main

import (
	"fmt"
	"net"
	keyboard "azul3d.org/engine/keyboard"
)

func main() {
	// connect to this socket
	conn, _ := net.Dial("tcp", "EDWIN-XPS15:12345")
	buf2 := make([]byte, 1024)
	defer conn.Close()

	for {
		msg := "none"
		watcher := keyboard.NewWatcher()
		// Query for the map containing information about all keys
		status := watcher.States()
		left := status[keyboard.ArrowLeft]
		if left == keyboard.Down {
			msg = "left"
		}
		buf := []byte(msg)
		_, err := conn.Write(buf) // Write a message to the server
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
