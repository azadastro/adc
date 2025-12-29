import re
from itertools import combinations
from z3 import Optimize, Ints, sat


lines = open("2025/inputs/10.txt").read().splitlines()

input_list = []
for line in lines:
    d_str, *b_str, j_str= line.split()
    input_list.append(
        {
            "diagram" : {i for i, c in enumerate(d_str[1:-1]) if c == "#"},
            "joltage" : list(map(int, j_str[1:-1].split(","))),
            "buttons" : [set(map(int, re.findall(r'\d', b))) for b in b_str]
        }
    )


def part_one(input_list):

    fewest_button = []
    for input in input_list:
        buttons = input["buttons"]
        diagram = input["diagram"]
        for combination_count in range(1, len(buttons)+1):
            for combination in combinations(buttons, r=combination_count):
                lights = set()
                for button in combination:
                    lights ^= button
                if lights == diagram:
                    fewest_button.append(combination_count)
                    break
            else:
                continue
            break

    print(sum(fewest_button))



def part_two(input_list):

    fewest_button = []
    for count, input in enumerate(input_list):
        buttons = input["buttons"]
        joltages = input["joltage"]
        
        variables = Ints(f"n_{i}" for i in range(len(buttons)))
        s = Optimize()
        for v in variables: s.add(v>=0)
        for i, joltage in enumerate(joltages):
            equation = 0
            for b, button in enumerate(buttons):
                if i in button:
                    equation += variables[b]
                            
            s.add(equation == joltage)
        
        s.minimize(sum(variables))
        s.check()
        fewest_button.append(s.model().eval(sum(variables)).as_long())      

    print(sum(fewest_button))


if __name__ == "__main__":

    print("Part One:")
    part_one(input_list)

    print("Part Two:")
    part_two(input_list)
