package main

import (
	"fmt"
	"time"
)

func main() {

	// TODO use 'make' to make a buffered channel, of size 5, that takes integers
	fmt.Printf("Capacity: %d\n", cap(ch))

	//TODO create an array of 5 integers using 'make'

	//TODO initialize the 5 indexes with values

	// TODO use 'go' to create a goroutine and pass in the channel and values
	fmt.Println("Sending value to channel")

	fmt.Println("Receiving from channel")

	// leave this
	time.Sleep(time.Second * 1)
}

func send(ch chan int, values []int) {
	// TODO send each value
}

func receive(ch chan int) {
	// TODO keep looping to receive all the values in the channel
	fmt.Printf("Value Received=%d in receive function\n", val)
}
