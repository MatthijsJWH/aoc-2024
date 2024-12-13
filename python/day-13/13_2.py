from typing import List
from pprint import pprint as pprint
from functools import cache

INPUT_FILE = "input.txt"
MAX_PRIZE = 401
DIFF = 10000000000000

class Button:
    def __init__(self, price: int, d_x: int, d_y: int):
        self.price = price
        self.d_x = d_x
        self.d_y = d_y

    def __repr__(self):
        return f"Button({self.price}, {self.d_x}, {self.d_y})"
    
    def __str__(self):
        return f"Button({self.price}, {self.d_x}, {self.d_y})"

class Prize:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Price({self.x}, {self.y})"
    
    def __str__(self):
        return f"Price({self.x}, {self.y})"

def readInput() -> List[str]:
    with open(INPUT_FILE, 'r') as f:
        return f.read().split('\n\n')
        
def parseInput(data: str) -> tuple[Prize, tuple[Button, Button]]:
    a, b, prize = data.splitlines()

    button_a = Button(3, int(a.split("X+")[1].split(",")[0]), int(a.split("Y+")[1]))
    button_b = Button(1, int(b.split("X+")[1].split(",")[0]), int(b.split("Y+")[1]))
    prize = Prize(int(prize.split("X=")[1].split(",")[0]) + DIFF, int(prize.split("Y=")[1]) + DIFF)

    return (prize, (button_a, button_b))

@cache
def getCost(prize: Prize, buttons: tuple[Button, Button]) -> int:
    b = (prize.x * buttons[0].d_y - prize.y * buttons[0].d_x) // (buttons[0].d_y * buttons[1].d_x - buttons[0].d_x * buttons[1].d_y)
    a = (prize.x * buttons[1].d_y - prize.y * buttons[1].d_x) // (buttons[1].d_y * buttons[0].d_x - buttons[1].d_x * buttons[0].d_y)

    if buttons[0].d_x * a + buttons[1].d_x * b == prize.x and buttons[0].d_y * a + buttons[1].d_y * b == prize.y:
        return a * buttons[0].price + b * buttons[1].price
              
    return 0
 
def costs(machines: List[tuple[Prize, tuple[Button, Button]]]) -> List[int]:
    costs = []

    for machine in machines:
        costs.append(getCost(machine[0], machine[1]))
    
    return costs
    
def main():
    data = readInput()
    machines = [parseInput(line) for line in data]
    costs_list = costs(machines)
    print(f"Result: {sum(costs_list)}")

if __name__ == "__main__":
    main()