package main

import (
	"os"
	"strconv"
	"strings"
)

func main() {
	input, _ := os.ReadFile("./input.txt")
	lines := strings.Split(string(input), "\n")

	count := 0
	last := -999

	for _, value := range lines {
		numb, _ := strconv.Atoi(strings.Trim(value, "\r"))

		//if ()

	}
}
