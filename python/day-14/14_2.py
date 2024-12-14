from typing import List
import numpy as np

EXAMPLE: bool = False

START: int = 7000

WIDTH: int = 11 if EXAMPLE else 101
HEIGHT: int = 7 if EXAMPLE else 103

INPUT_FILE: str = "e_input.txt" if EXAMPLE else "input.txt"

class Robot:
    def __init__(self, x: int, y: int, v_x: int, v_y: int):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

        if self.x < 0:
            self.x = WIDTH + self.x
        if self.y < 0:
            self.y = HEIGHT + self.y

        if self.x >= WIDTH:
            self.x -= WIDTH
        if self.y >= HEIGHT:
            self.y -= HEIGHT

    def __str__(self):
        return f"Robot: x={self.x}, y={self.y}, v_x={self.v_x}, v_y={self.v_y}"

    def __repr__(self):
        return self.__str__()

def read_input() -> List[str]:
    with open(INPUT_FILE, "r") as f:
        return f.read().splitlines()

def parse_input(input: List[str]) -> List[Robot]:
    robots: List[Robot] = []
    for line in input:
        line = line.split(" ")

        pos = line[0][2:].split(",")
        x, y = int(pos[0]), int(pos[1])
        velo = line[1][2:].split(",")
        v_x, v_y = int(velo[0]), int(velo[1])

        robots.append(Robot(x, y, v_x, v_y))

    return robots

def predict(robots: List[Robot], seconds: int) -> List[Robot]:
    for i in range(seconds):
        for robot in robots:
            robot.move()

    return robots

def print_grid(robots: List[Robot]):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            r = 0
            for robot in robots:
                if robot.x == x and robot.y == y:
                    r += 1

            if r == 0:
                print(" ", end="")
            else:
                print("#", end="")
        print()

def main():
    robots = parse_input(read_input())
    r = robots

    r = predict(r, START)

    for i in range(START, 101*103):
        r = predict(r, 1)
        var_x = np.var([robot.x for robot in r])
        var_y = np.var([robot.y for robot in r])

        if var_x < 500 and var_y < 500:
            print(f'Found at {i+1}')
            print_grid(r)

if __name__ == "__main__":
    main()
