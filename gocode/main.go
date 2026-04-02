package main

import (
	"fmt"
	"time"
	"strconv"
)

func main() {
	fmt.Println("vim-go")
	i := 0
	for {
		fmt.Println("Hi Hind: " + strconv.Itoa(i))
		time.Sleep(15 * time.Second)
		i=i+1

	}
}
