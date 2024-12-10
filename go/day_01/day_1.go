package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
)

func main() {
	// Parse and format the input
	s := time.Now()
	input := parseInput("input.txt")
	nums1, nums2 := formatInput(input)
	fmt.Println("Parse and Format Time: ", time.Since(s))

	// Part 1
	p1 := time.Now()
	fmt.Println("Part 1: ", part1(nums1, nums2), "Time: ", time.Since(p1))

	// Part 2
	p2 := time.Now()
	fmt.Println("Part 2: ", part2(nums1, nums2), "Time: ", time.Since(p2))
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

func formatInput(input []string) ([]int, []int) {
	var nums1 []int
	var nums2 []int

	for _, line := range input {
		// Split the line into two numbers
		// Convert the numbers to integers
		// Append the numbers to the respective slice
		l := strings.Split(line, "   ")
		n1, err := strconv.Atoi(l[0])
		if err != nil {
			fmt.Println("Error: ", err)
			return nil, nil
		}
		n2, err := strconv.Atoi(l[1])
		if err != nil {
			fmt.Println("Error: ", err)
			return nil, nil
		}
		nums1 = append(nums1, n1)
		nums2 = append(nums2, n2)
	}

	return nums1, nums2

}

func part1(nums1 []int, nums2 []int) int {
	if len(nums1) != len(nums2) {
		fmt.Println("Error: Slices are not the same length")
	}

	sort.Ints(nums1)
	sort.Ints(nums2)

	result := 0

	for i := 0; i < len(nums1); i++ {
		i := nums1[i] - nums2[i]
		if i < 0 {
			i = i * -1
		}
		result += i
	}

	return result
}

func part2(nums1 []int, nums2 []int) int {
	map1, map2 := make(map[int]int), make(map[int]int)

	for _, num := range nums1 {
		map1[num]++
	}

	for _, num := range nums2 {
		map2[num]++
	}

	result := 0

	for k, v := range map1 {
		result += k * v * map2[k]
	}

	return result
}
