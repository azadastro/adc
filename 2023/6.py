
import re
from collections import defaultdict

with open("6.txt", "r") as f:
    lines = f.readlines()


def part_one():

    inputs = defaultdict(list)
    for line in lines:
        line = line.replace("\n", "")
        
        dict_key, numbers = line.split(":")
        inputs[dict_key] = [int(n.group()) for n in list(re.finditer(r"\d+", numbers))]

    mult_num_try = 1
    for time, distance in zip(inputs["Time"], inputs["Distance"]):
        
        num_try = 0
        for hld_t in range(time+1):
            dist_travel = (time - hld_t) * hld_t
            if dist_travel > distance:
                num_try += 1
        mult_num_try *= num_try

    print(mult_num_try)


def part_two():

    inputs = defaultdict(list)
    for line in lines:
        line = line.replace("\n", "").replace(" ", "")
        
        dict_key, numbers = line.split(":")
        inputs[dict_key] = int(numbers)

    time, distance = inputs["Time"], inputs["Distance"]
        
    num_try = 0
    for hld_t in range(time+1):
        dist_travel = (time - hld_t) * hld_t
        if dist_travel > distance:
            num_try += 1

    print(num_try)



if __name__ == "__main__":
    
    part_one()
    part_two()