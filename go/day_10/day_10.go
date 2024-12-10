package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type Point struct {
	x int
	y int
}

type scoreCalculation func([][]int, Point) []Point

func parseInput(fileName string) [][]int {
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Println("Error: ", err)
		return nil
	}
	defer file.Close()
	r := bufio.NewReader(file)

	var lines [][]int
	for {
		line, _, err := r.ReadLine()

		if err != nil {
			break
		}

		var values []int

		for _, part := range strings.Split(string(line), "") {
			h, _ := strconv.Atoi(part)
			values = append(values, h)
		}
		lines = append(lines, values)
	}

	return lines
}

func getTrailheads(grid [][]int) []Point {
	trailheads := []Point{}

	for i, row := range grid {
		for j, cell := range row {
			if cell == 0 {
				trailheads = append(trailheads, Point{i, j})
			}
		}
	}

	return trailheads
}

func getScores(grid [][]int, trailheads []Point, f scoreCalculation) []int {
	scores := []int{}

	for _, trailhead := range trailheads {
		score := f(grid, trailhead)
		scores = append(scores, len(score))
	}

	return scores
}

func uniqueScores(grid [][]int, trailhead Point) []Point {
	height := grid[trailhead.x][trailhead.y]
	if height == 9 {
		return []Point{{trailhead.x, trailhead.y}}
	}

	trails := []Point{}

	directions := []Point{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	for _, direction := range directions {
		x := trailhead.x + direction.x
		y := trailhead.y + direction.y

		if x < 0 || x >= len(grid) || y < 0 || y >= len(grid[0]) {
			continue
		}

		if grid[x][y] == height+1 {
			for _, trail := range uniqueScores(grid, Point{x, y}) {
				check := false

				for _, p := range trails {
					if p.x == trail.x && p.y == trail.y {
						check = true
					}
				}

				if check {
					continue
				}

				trails = append(trails, trail)
			}
		}
	}

	return trails
}

func dupScores(grid [][]int, trailhead Point) []Point {
	height := grid[trailhead.x][trailhead.y]
	if height == 9 {
		return []Point{{trailhead.x, trailhead.y}}
	}

	trails := []Point{}

	directions := []Point{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	for _, direction := range directions {
		x := trailhead.x + direction.x
		y := trailhead.y + direction.y

		if x < 0 || x >= len(grid) || y < 0 || y >= len(grid[0]) {
			continue
		}

		if grid[x][y] == height+1 {
			trails = append(trails, dupScores(grid, Point{x, y})...)
		}
	}

	return trails
}

func part1(grid [][]int) int {
	trailheads := getTrailheads(grid)
	scores := getScores(grid, trailheads, uniqueScores)

	sum := 0
	for _, score := range scores {
		sum += score
	}

	return sum
}

func part2(grid [][]int) int {
	trailheads := getTrailheads(grid)
	scores := getScores(grid, trailheads, dupScores)

	sum := 0
	for _, score := range scores {
		sum += score
	}

	return sum
}

func main() {
	start := time.Now()
	fileName := "input.txt"
	grid := parseInput(fileName)
	fmt.Println("Part 1: ", part1(grid))
	fmt.Println("Part 2: ", part2(grid))
	fmt.Println("Execution time: ", time.Since(start))
}
