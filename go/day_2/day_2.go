package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func main() {
	// Parse and format the input
	s := time.Now()
	input := parseInput("input.txt")
	reports := formatInput(input)
	// fmt.Println("Reports: ", reports)
	fmt.Println("Parse and Format Time: ", time.Since(s))

	// Part 1
	p1 := time.Now()
	fmt.Println("Part 1: ", part1(reports), "Time: ", time.Since(p1))

	// Part 2
	p2 := time.Now()
	fmt.Println("Part 2: ", part2(reports), "Time: ", time.Since(p2))
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
			fmt.Println("Error: ", err)
			break
		}
	}

	return lines
}

func formatInput(input []string) [][]int {
	var nums [][]int

	for i, line := range input {
		// Split the line into two numbers
		// Convert the numbers to integers
		// Append the numbers to the respective slice
		l := strings.Split(line, " ")
		nums = append(nums, []int{})
		for _, num := range l {
			n, _ := strconv.Atoi(num)
			nums[i] = append(nums[i], n)
		}
	}

	return nums

}

func part1(reports [][]int) int {
	result := 0

	for _, report := range reports {
		asc := checkAscending(report)
		if checkSafe(report, asc) {
			result++
		}
	}

	return result
}

func part2(reports [][]int) int {
	result := 0

	for _, report := range reports {
		asc := checkAscending(report)

		if checkSafe(report, asc) {
			result++
			continue
		}

		for i := 0; i < len(report)-1; i++ {
			c := make([]int, len(report))
			copy(c, report)
			r := append(c[:i], c[i+1:]...)
			if checkSafe(r, asc) {
				result++
				break
			}
		}
	}

	return result
}

func checkAscending(report []int) bool {
	return report[0] <= report[1]
}

func checkSafe(report []int, asc bool) bool {
	for i := range report {
		switch i {
		case len(report) - 1:
			return true
		default:
			t := report[i+1] - report[i]
			if t < -3 || t == 0 || t > 3 {
				return false
			}
			if t > 0 && !asc {
				return false
			}
			if t < 0 && asc {
				return false
			}
		}
	}

	return false
}
