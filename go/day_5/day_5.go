package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"sort"
	"strconv"
	"strings"
	"time"
)

var ORDERING_RULES map[int][]int = make(map[int][]int)

type IntSlice []int

func (s IntSlice) Len() int {
	return len(s)
}

func (s IntSlice) Less(i, j int) bool {
	x, ok_x := ORDERING_RULES[s[i]]
	y, ok_y := ORDERING_RULES[s[j]]
	if ok_x {
		return slices.Contains(x, s[j])
	}
	if ok_y {
		if slices.Contains(y, s[i]) {
			return false
		}
	}

	return false
}

func (s IntSlice) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
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
		lines = append(lines, string(line))
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

func formatInput(input []string) (map[int][]int, [][]int) {
	ordering_rules := make(map[int][]int)
	updates := make([][]int, 0)

	for _, line := range input {
		if line == "" {
			continue
		}

		if strings.Contains(line, "|") {
			s := strings.Split(line, "|")
			x, _ := strconv.Atoi(s[0])
			y, _ := strconv.Atoi(s[1])
			ordering_rules[x] = append(ordering_rules[x], y)
		} else {
			update := make([]int, 0)
			s := strings.Split(line, ",")
			for _, v := range s {
				num, _ := strconv.Atoi(v)
				update = append(update, num)
			}
			updates = append(updates, update)
		}
	}

	return ordering_rules, updates
}

func isValidUpdate(update []int) bool {
	for i, x := range update {
		for _, y := range update[i+1:] {
			l, ok := ORDERING_RULES[y]
			if !ok {
				continue
			}
			if slices.Contains(l, x) {
				return false
			}
		}
	}

	return true
}

func getValidUpdates(updates [][]int) [][]int {
	valid_updates := make([][]int, 0)

	for _, update := range updates {
		if isValidUpdate(update) {
			valid_updates = append(valid_updates, update)
		}
	}

	return valid_updates
}

func countMiddleValues(updates [][]int) int {
	count := 0

	for _, update := range updates {
		mid_index := len(update) / 2
		count += update[mid_index]
	}

	return count
}

func sliceDifference(a, b [][]int) [][]int {
	diff := make([][]int, 0)
	for _, x := range a {
		if !containsSlice(b, x) {
			diff = append(diff, x)
		}
	}

	return diff
}

func containsSlice(slices [][]int, slice []int) bool {
	for _, s := range slices {
		if equalSlices(s, slice) {
			return true
		}
	}
	return false
}

func equalSlices(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i, v := range a {
		if v != b[i] {
			return false
		}
	}
	return true
}

func orderUpdates(updates [][]int) [][]int {
	ordered_updates := make([][]int, len(updates))
	for i, update := range updates {
		ordered_updates[i] = make([]int, len(update))
		is := IntSlice(update)
		sort.Sort(is)
		ordered_updates[i] = is
	}
	return ordered_updates
}

func part1(updates [][]int) int {
	valid_updates := getValidUpdates(updates)
	return countMiddleValues(valid_updates)
}

func part2(updates [][]int) int {
	invalid_updates := sliceDifference(updates, getValidUpdates(updates))
	ordered_updates := orderUpdates(invalid_updates)
	return countMiddleValues(ordered_updates)
}

func main() {
	input_file := "input.txt"

	s := time.Now()
	input := parseInput(input_file)
	ordering_rules, updates := formatInput(input)
	ORDERING_RULES = ordering_rules

	fmt.Printf("Parse and Format Time: %v\n", time.Since(s))

	// Part 1
	p1 := time.Now()
	fmt.Printf("Part 1: %d, Time: %v\n", part1(updates), time.Since(p1))

	// Part 2
	p2 := time.Now()
	fmt.Printf("Part 2: %d, Time: %v\n", part2(updates), time.Since(p2))
}
