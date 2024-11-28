import re
from collections import defaultdict

with open("8.txt", "r") as f:
        lines = f.readlines()

def get_inputs():

    moves = lines[0].replace("\n", "")
    map_dict = {}
    for line in lines[2:]:
         line = line.replace("\n", "")
         key, map = line.split("=")
         l, r = map.replace(" ", "").replace("(", "").replace(")", "").split(",")
         map_dict[key.strip()] = (l, r)

    return moves, map_dict

def part_one(moves, maps_dict):
     
    i = 0
    cur_step = "AAA"
    steps = 0
    while True:
        map_move = maps_dict[cur_step]
        m = 0 if moves[i] == "L" else 1
        if i == len(moves)-1:
            i = 0
        else:
            i += 1

        cur_step = map_move[m]
        if cur_step == "ZZZ":
            print(steps+1)
            break
        else:
            steps += 1


def part_two(moves, maps_dict):
    i = 0
    strt_step = []
    fin_step = []

    for maps in maps_dict.keys():
        if maps[-1] == "A":
            strt_step.append(maps)
        if maps[-1] == "Z":
            fin_step.append(maps)

    steps = 0
    while True:

        
        m = 0 if moves[i] == "L" else 1
        next_step = []
        for s in strt_step:
            map_move = maps_dict[s]
            next_step.append(map_move[m])

        cur_step = next_step
        if len(set(cur_step).intersection(set(fin_step))) == len(fin_step):
            print(steps+1)
            break
        else:
            steps += 1

        if i == len(moves)-1:
            i = 0
        else:
            i += 1


if __name__ == "__main__":
    
    moves, inputs = get_inputs()
    #part_one(moves, inputs)
    part_two(moves, inputs)