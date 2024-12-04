package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"time"
)

func main() {
	// Parse and format the input
	s := time.Now()
	input := parseInput("input.txt")
	fmt.Println("Parse and Format Time: ", time.Since(s))

	// Part 1
	p1 := time.Now()
	fmt.Printf("Part 1: %d, Time: %v\n", part1(input), time.Since(p1))

	// Part 2
	p2 := time.Now()
	fmt.Printf("Part 2: %d, Time: %v\n", part2(input), time.Since(p2))
}

func parseInput(fileName string) []string {
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println("Error: ", err)
		return nil
	}
	defer file.Close()
	r := bufio.NewReader(file)

	var lines []string
	for {
		line, _, err := r.ReadLine()
		if len(line) > 0 {
			lines = append(lines, string(line))
		}
		if err != nil {
			if err.Error() == "EOF" {
				break
			}
			fmt.Println("Error: ", err)
			break
		}
	}
	return lines
}

func part1(data []string) int {
	r, _ := regexp.Compile(`mul\([0-9]{1,3},[0-9]{1,3}\)`)
	instructions := make([]string, 0)

	for _, line := range data {
		instructions = append(instructions, r.FindAllString(line, -1)...)
	}

	result := 0

	for _, instruction := range instructions {
		a, b := 0, 0
		if _, err := fmt.Sscanf(instruction, "mul(%d,%d)", &a, &b); err != nil {
			fmt.Println("Error parsing instruction: ", err)
			continue
		}
		result += a * b
	}

	return result
}

func part2(data []string) int {
	r, _ := regexp.Compile(`(mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\))`)
	instructions := make([]string, 0)

	for _, line := range data {
		instructions = append(instructions, r.FindAllString(line, -1)...)
	}

	result := 0
	do := true

	for _, instruction := range instructions {
		switch instruction {
		case "do()":
			do = true
		case "don't()":
			do = false
		default:
			if do {
				a, b := 0, 0
				if _, err := fmt.Sscanf(instruction, "mul(%d,%d)", &a, &b); err != nil {
					fmt.Println("Error parsing instruction: ", err)
					continue
				}
				result += a * b
			}
		}
	}

	return result
}
