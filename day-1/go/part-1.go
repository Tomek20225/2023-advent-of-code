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
		return
	}
	defer readFile.Close()

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	var sum int

	for fileScanner.Scan() {
		line := fileScanner.Text()
		nums := make([]int, 0)

		for _, char := range line {
			if unicode.IsDigit(rune(char)) {
				digit, err := strconv.Atoi(string(char))
				if err != nil {
					fmt.Println(err)
					return
				}
				nums = append(nums, digit)
			}
		}

		if len(nums) >= 1 {
			first := nums[0]
			last := nums[len(nums) - 1]
			val := (first * 10) + last
			sum += val
		}
	}

	fmt.Println(sum)
}