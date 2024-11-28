import re
from collections import defaultdict

lines = open("9.txt").read().splitlines()

input_list = []
for line in lines:
    input_list.append(list(map(int, line.split())))

def part_one():
    
    next_value = []
    for l in input_list:

        next_line = []
        next_line.append(l)
        while True:
            temp = []
            for i in range(len(l)-1):
                temp.append(l[i+1] - l[i])

            l = temp
            next_line.append(temp)
            if all(x == 0 for x in temp):
                break

        num = 0
        for i in range(len(next_line), 0, -1):
            num += next_line[i-1][-1]
        next_value.append(num)

    print(sum(next_value))



def part_two():
    next_value = []
    for l in input_list:

        next_line = []
        next_line.append(l)
        while True:
            temp = []
            for i in range(len(l)-1):
                temp.append(l[i+1] - l[i])

            l = temp
            if all(x == 0 for x in temp):
                break

            next_line.append(temp)

        num = 0
        for i in range(len(next_line), 0, -1):
            num = next_line[i-1][0] - num

        next_value.append(num)

    print(sum(next_value))


if __name__ == "__main__":

    part_one()
    part_two()