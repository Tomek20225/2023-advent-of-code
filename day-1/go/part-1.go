package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"unicode"
)

func main() {
	readFile, err := os.Open("../input.txt")

	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	var sum int

	for fileScanner.Scan() {
		line := fileScanner.Text()
		nums := make([]int, 0)

		for i := 0; i < len(line); i++ {
			char := line[i]
			if unicode.IsDigit(rune(char)) {
				int, err := strconv.Atoi(string(char))
				if err != nil {
					return
				}
				nums = append(nums, int)
			}
		}

		first := nums[0]
		last := nums[len(nums) - 1]
		val := (first * 10) + last

		sum += val
	}

	fmt.Println(sum)

	readFile.Close()
}