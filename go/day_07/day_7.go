package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type equation struct {
	answer int
	values []int
}

func parseInput(fileName string) []equation {
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println("Error: ", err)
		return nil
	}
	defer file.Close()
	r := bufio.NewReader(file)

	var lines []equation
	for {
		line, _, err := r.ReadLine()

		if err != nil {
			break
		}

		parts := strings.Split(string(line), ": ")
		if len(parts) < 2 {
			break
		}
		answer, _ := strconv.Atoi(parts[0])
		values := []int{}
		for _, part := range strings.Split(parts[1], " ") {
			dependency, _ := strconv.Atoi(part)
			values = append(values, dependency)
		}
		lines = append(lines, equation{answer, values})
	}
	return lines
}

func checkValidAnswerPartOne(answer int, values []int) bool {
	if len(values) == 1 {
		return values[0] == answer
	}

	check := checkValidAnswerPartOne(answer, append([]int{values[0] + values[1]}, values[2:]...))
	if check {
		return true
	}

	check = checkValidAnswerPartOne(answer, append([]int{values[0] * values[1]}, values[2:]...))
	return check
}

func part1(lines []equation) int {
	sum := 0

	for _, line := range lines {
		if checkValidAnswerPartOne(line.answer, line.values) {
			sum += line.answer
		}
	}

	return sum
}

func checkValidAnswerPartTwo(answer int, values []int) bool {
	if len(values) == 1 {
		return values[0] == answer
	}

	check := checkValidAnswerPartTwo(answer, append([]int{values[0] + values[1]}, values[2:]...))
	if check {
		return true
	}

	check = checkValidAnswerPartTwo(answer, append([]int{values[0] * values[1]}, values[2:]...))

	if check {
		return true
	}

	temp, _ := strconv.Atoi(strconv.Itoa(values[0]) + strconv.Itoa(values[1]))
	check = checkValidAnswerPartTwo(answer, append([]int{temp}, values[2:]...))
	return check
}

func part2(lines []equation) int {
	sum := 0

	for _, line := range lines {
		if checkValidAnswerPartTwo(line.answer, line.values) {
			sum += line.answer
		}
	}

	return sum
}

func main() {
	start := time.Now()
	fileName := "input.txt"
	lines := parseInput(fileName)
	fmt.Println("Part 1: ", part1(lines))
	fmt.Println("Part 2: ", part2(lines))
	fmt.Println("Execution time: ", time.Since(start))
}
